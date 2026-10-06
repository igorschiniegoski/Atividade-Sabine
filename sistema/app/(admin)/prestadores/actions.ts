"use server";

import { Prisma } from "@prisma/client";
import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { prisma } from "@/lib/db";
import { exigirPerfil } from "@/lib/permissao";
import { prestadorSchema } from "@/lib/validacao/prestador";

export type EstadoFormulario = {
  erros?: Record<string, string[] | undefined>;
  mensagem?: string;
  valores?: Record<string, string>;
};

// UC03 - manter prestador. id nulo = cadastro novo, com id = edicao
export async function salvarPrestador(
  id: number | null,
  _estado: EstadoFormulario,
  form: FormData,
): Promise<EstadoFormulario> {
  const usuario = await exigirPerfil("administrador");

  const valores = Object.fromEntries(form) as Record<string, string>;
  const validacao = prestadorSchema.safeParse(valores);

  if (!validacao.success) {
    return {
      erros: validacao.error.flatten().fieldErrors,
      mensagem: "Confira os campos destacados.",
      valores,
    };
  }

  const dados = validacao.data;

  try {
    if (id === null) {
      // todo prestador novo nasce pendente (dicionario de dados) e o primeiro registro
      // do historico de situacao ja e gravado junto, na mesma operacao
      await prisma.prestador.create({
        data: {
          ...dados,
          historicos: {
            create: {
              situacao_anterior: null,
              situacao_nova: "pendente",
              motivo: "cadastro inicial do prestador",
              id_usuario: Number(usuario.id),
            },
          },
        },
      });
    } else {
      await prisma.prestador.update({
        where: { id_prestador: id },
        data: { ...dados, atualizado_em: new Date() },
      });
    }
  } catch (erro) {
    // RN10: o banco tem unique em cpf_cnpj, entao um cadastro repetido cai aqui
    if (erro instanceof Prisma.PrismaClientKnownRequestError && erro.code === "P2002") {
      const nome = dados.tipo_pessoa === "F" ? "CPF" : "CNPJ";
      return {
        erros: { cpf_cnpj: [`Já existe um prestador cadastrado com este ${nome}.`] },
        mensagem: "Confira os campos destacados.",
        valores,
      };
    }
    throw erro;
  }

  revalidatePath("/prestadores");
  redirect(`/prestadores?salvo=${id === null ? "novo" : "editado"}`);
}

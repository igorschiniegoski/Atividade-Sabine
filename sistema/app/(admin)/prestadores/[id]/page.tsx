import { notFound } from "next/navigation";
import { prisma } from "@/lib/db";
import { exigirPerfil } from "@/lib/permissao";
import { formatarCpfCnpj } from "@/lib/dominio/cpf-cnpj";
import { AbasPrestador } from "../abas";
import { FormularioPrestador } from "../formulario";
import { Situacao } from "../situacao";

// T04 - cadastro do prestador (edicao)
export default async function EditarPrestador({ params }: { params: Promise<{ id: string }> }) {
  await exigirPerfil("administrador");
  const { id } = await params;

  const prestador = await prisma.prestador.findUnique({ where: { id_prestador: Number(id) || 0 } });
  if (!prestador) notFound();

  // o formulario trabalha com texto. campos nulos viram vazio
  const inicial: Record<string, string> = {};
  for (const [campo, valor] of Object.entries(prestador)) {
    inicial[campo] = valor === null ? "" : String(valor);
  }
  inicial.cpf_cnpj = formatarCpfCnpj(prestador.cpf_cnpj);
  inicial.cep = prestador.cep.replace(/(\d{5})(\d{3})/, "$1-$2");

  return (
    <div className="mx-auto max-w-5xl">
      <div className="mb-4 flex flex-wrap items-start justify-between gap-2 border-b border-regua pb-3">
        <div>
          <h1 className="text-xl font-semibold">{prestador.nome_fantasia ?? prestador.nome_razao_social}</h1>
          <p className="text-sm text-tinta2">Cadastro do prestador</p>
        </div>
        <Situacao valor={prestador.situacao} />
      </div>
      <AbasPrestador />
      <FormularioPrestador id={prestador.id_prestador} inicial={inicial} />
    </div>
  );
}

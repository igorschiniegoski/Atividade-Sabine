import Link from "next/link";
import { Prisma } from "@prisma/client";
import { prisma } from "@/lib/db";
import { exigirPerfil } from "@/lib/permissao";
import { formatarCpfCnpj, soDigitos } from "@/lib/dominio/cpf-cnpj";
import { SITUACOES } from "@/lib/validacao/prestador";
import { Situacao } from "./situacao";

// RNF06: a listagem e paginada no banco, nunca trazendo tudo de uma vez
const POR_PAGINA = 20;

type Busca = { busca?: string; situacao?: string; pagina?: string; salvo?: string };

// T03 - prestadores
export default async function Prestadores({ searchParams }: { searchParams: Promise<Busca> }) {
  await exigirPerfil("administrador");
  const params = await searchParams;

  const busca = (params.busca ?? "").trim();
  const situacao = SITUACOES.includes(params.situacao as never) ? params.situacao : "";
  const pagina = Math.max(1, Number(params.pagina) || 1);

  const filtro: Prisma.prestadorWhereInput = {};
  if (situacao) filtro.situacao = situacao;
  if (busca) {
    const digitos = soDigitos(busca);
    filtro.OR = [
      { nome_razao_social: { contains: busca, mode: "insensitive" } },
      { nome_fantasia: { contains: busca, mode: "insensitive" } },
      ...(digitos.length >= 3 ? [{ cpf_cnpj: { contains: digitos } }] : []),
    ];
  }

  const [total, prestadores] = await Promise.all([
    prisma.prestador.count({ where: filtro }),
    prisma.prestador.findMany({
      where: filtro,
      orderBy: { nome_razao_social: "asc" },
      skip: (pagina - 1) * POR_PAGINA,
      take: POR_PAGINA,
    }),
  ]);
  const paginas = Math.max(1, Math.ceil(total / POR_PAGINA));

  function linkPagina(p: number) {
    const q = new URLSearchParams();
    if (busca) q.set("busca", busca);
    if (situacao) q.set("situacao", situacao);
    q.set("pagina", String(p));
    return `/prestadores?${q}`;
  }

  return (
    <div className="mx-auto max-w-6xl">
      <div className="mb-4 flex flex-wrap items-start justify-between gap-3 border-b border-regua pb-3">
        <div>
          <h1 className="text-xl font-semibold">Prestadores</h1>
          <p className="text-sm text-tinta2">Cadastro da rede de terceirizados</p>
        </div>
        <Link href="/prestadores/novo" className="botao-principal">Novo prestador</Link>
      </div>

      {params.salvo && (
        <p className="mb-4 rounded border-l-3 border-verde bg-verde-fundo px-3 py-2 text-sm text-verde" role="status">
          {params.salvo === "novo" ? "Prestador cadastrado. Ele entra como pendente até a documentação ser conferida." : "Alterações salvas."}
        </p>
      )}

      <form className="cartao mb-4 flex flex-wrap items-end gap-3 p-4">
        <div className="min-w-56 flex-1">
          <label htmlFor="busca" className="rotulo">Buscar</label>
          <input id="busca" name="busca" defaultValue={busca} placeholder="Nome, razão social, CPF ou CNPJ" className="campo" />
        </div>
        <div className="w-40">
          <label htmlFor="situacao" className="rotulo">Situação</label>
          <select id="situacao" name="situacao" defaultValue={situacao} className="campo">
            <option value="">Todas</option>
            {SITUACOES.map((s) => (
              <option key={s} value={s} className="capitalize">{s[0].toUpperCase() + s.slice(1)}</option>
            ))}
          </select>
        </div>
        <button className="botao">Filtrar</button>
      </form>

      <div className="cartao overflow-x-auto">
        <p className="cartao-titulo">
          {total === 1 ? "1 prestador encontrado" : `${total} prestadores encontrados`}
        </p>
        {prestadores.length === 0 ? (
          <p className="px-4 py-6 text-sm text-tinta2">
            Nenhum prestador com esse filtro. {!busca && !situacao && "Use o botão Novo prestador para cadastrar o primeiro."}
          </p>
        ) : (
          <table className="w-full min-w-[640px] text-sm">
            <thead>
              <tr className="border-b border-regua-clara text-left text-xs text-tinta2">
                <th className="px-4 py-2 font-semibold">Prestador</th>
                <th className="px-4 py-2 font-semibold">CPF / CNPJ</th>
                <th className="px-4 py-2 font-semibold">Situação</th>
                <th className="px-4 py-2"></th>
              </tr>
            </thead>
            <tbody>
              {prestadores.map((p) => (
                <tr key={p.id_prestador} className="border-b border-regua-clara last:border-0 hover:bg-[#faf9f7]">
                  <td className="px-4 py-2">
                    <p>{p.nome_razao_social}</p>
                    <p className="text-xs text-tinta2">
                      {p.nome_fantasia ?? (p.tipo_pessoa === "F" ? "autônomo" : "sem nome fantasia")}, {p.telefone}
                    </p>
                  </td>
                  <td className="whitespace-nowrap px-4 py-2 tabular-nums">{formatarCpfCnpj(p.cpf_cnpj)}</td>
                  <td className="px-4 py-2"><Situacao valor={p.situacao} /></td>
                  <td className="px-4 py-2 text-right">
                    <Link href={`/prestadores/${p.id_prestador}`} className="botao py-1">Abrir</Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>

      {paginas > 1 && (
        <div className="mt-3 flex items-center justify-end gap-2 text-sm">
          {pagina > 1 && <Link href={linkPagina(pagina - 1)} className="botao py-1">Anterior</Link>}
          <span className="text-tinta2">Página {pagina} de {paginas}</span>
          {pagina < paginas && <Link href={linkPagina(pagina + 1)} className="botao py-1">Próxima</Link>}
        </div>
      )}
    </div>
  );
}

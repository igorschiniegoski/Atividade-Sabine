"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

// itens sem href ainda nao foram implementados. ficam no menu (so no computador) pra mostrar o que vem,
// mas marcados como em desenvolvimento e sem clique
const grupos = [
  {
    titulo: "Operação",
    itens: [{ nome: "Painel do dia" }, { nome: "Ordens de serviço" }, { nome: "Vencimentos" }],
  },
  {
    titulo: "Cadastro",
    itens: [
      { nome: "Prestadores", href: "/prestadores" },
      { nome: "Clientes" },
      { nome: "Serviços" },
      { nome: "Categorias" },
    ],
  },
];

export function MenuLateral() {
  const caminho = usePathname();

  return (
    <nav className="flex min-w-0 gap-4 overflow-x-auto border-b border-regua bg-white px-3 py-2 md:block md:w-52 md:shrink-0 md:overflow-visible md:border-r md:border-b-0 md:px-0 md:py-4">
      {grupos.map((grupo) => (
        <div key={grupo.titulo} className="flex shrink-0 items-center gap-1 md:mb-4 md:block">
          <p className="hidden px-4 pb-1 text-xs font-semibold text-tinta2 md:block">{grupo.titulo}</p>
          {grupo.itens.map((item) =>
            item.href ? (
              <Link
                key={item.nome}
                href={item.href}
                className={`block whitespace-nowrap px-4 py-1.5 text-sm ${
                  caminho.startsWith(item.href)
                    ? "border-l-3 border-caneta bg-caneta-clara font-semibold"
                    : "hover:bg-papel"
                }`}
              >
                {item.nome}
              </Link>
            ) : (
              <span
                key={item.nome}
                title="Em desenvolvimento"
                className="hidden whitespace-nowrap px-4 py-1.5 text-sm text-[#a3a8ad] md:block"
              >
                {item.nome} <span className="text-[10px] uppercase">em desenv.</span>
              </span>
            ),
          )}
        </div>
      ))}
    </nav>
  );
}

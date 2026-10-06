const cores: Record<string, string> = {
  ativo: "border-verde bg-verde-fundo text-verde",
  pendente: "border-ocre bg-ocre-fundo text-ocre",
  bloqueado: "border-carimbo bg-carimbo-fundo text-carimbo",
  inativo: "border-ardosia bg-ardosia-fundo text-ardosia",
};

export function Situacao({ valor }: { valor: string }) {
  return (
    <span className={`inline-block rounded-sm border-l-3 px-1.5 py-0.5 text-xs font-semibold capitalize ${cores[valor] ?? ""}`}>
      {valor}
    </span>
  );
}

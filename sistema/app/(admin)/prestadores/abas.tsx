// abas da T04. so "dados cadastrais" existe nesta entrega, as outras entram nas proximas
const abas = ["Dados cadastrais", "Categorias", "Documentos", "Situação cadastral"];

export function AbasPrestador() {
  return (
    <div className="mb-4 flex flex-wrap gap-1 border-b border-regua text-sm">
      {abas.map((aba, i) =>
        i === 0 ? (
          <span key={aba} className="-mb-px whitespace-nowrap rounded-t border border-b-0 border-regua border-t-caneta border-t-2 bg-white px-4 py-2 font-semibold">
            {aba}
          </span>
        ) : (
          <span key={aba} title="Em desenvolvimento" className="whitespace-nowrap px-4 py-2 text-[#a3a8ad]">
            {aba} <span className="text-[10px] uppercase">em desenv.</span>
          </span>
        ),
      )}
    </div>
  );
}

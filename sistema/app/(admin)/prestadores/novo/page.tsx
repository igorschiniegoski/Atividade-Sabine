import { exigirPerfil } from "@/lib/permissao";
import { AbasPrestador } from "../abas";
import { FormularioPrestador } from "../formulario";

// T04 - cadastro do prestador (novo)
export default async function NovoPrestador() {
  await exigirPerfil("administrador");

  return (
    <div className="mx-auto max-w-5xl">
      <div className="mb-4 border-b border-regua pb-3">
        <h1 className="text-xl font-semibold">Novo prestador</h1>
        <p className="text-sm text-tinta2">Cadastro do prestador</p>
      </div>
      <AbasPrestador />
      <FormularioPrestador id={null} />
    </div>
  );
}

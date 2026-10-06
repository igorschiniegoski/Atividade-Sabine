import { signOut } from "@/auth";

export default function SemPermissao() {
  return (
    <main className="flex min-h-screen items-center justify-center px-4">
      <div className="cartao max-w-md p-6">
        <h1 className="mb-2 text-lg font-semibold">Acesso não liberado</h1>
        <p className="mb-4 text-sm text-tinta2">
          Seu perfil não tem permissão para esta área. As telas de prestador e de cliente ainda estão em desenvolvimento.
        </p>
        <form action={async () => { "use server"; await signOut({ redirectTo: "/login" }); }}>
          <button className="botao">Sair</button>
        </form>
      </div>
    </main>
  );
}

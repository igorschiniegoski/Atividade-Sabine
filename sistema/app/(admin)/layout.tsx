import { signOut } from "@/auth";
import { exigirPerfil } from "@/lib/permissao";
import { MenuLateral } from "./menu-lateral";

export default async function LayoutAdmin({ children }: { children: React.ReactNode }) {
  const usuario = await exigirPerfil("administrador");

  return (
    <div className="flex min-h-screen flex-col">
      <header className="flex items-center justify-between border-b-3 border-caneta bg-caneta-escura px-4 py-2 text-white">
        <div className="flex items-baseline gap-2">
          <span className="text-lg font-bold">SGP</span>
          <span className="hidden text-sm text-[#aab0b6] sm:inline">gestão de prestadores</span>
        </div>
        <div className="flex items-center gap-3">
          <div className="text-right leading-tight">
            <p className="text-sm font-semibold">{usuario.name}</p>
            <p className="text-xs text-[#aab0b6]">Administrador</p>
          </div>
          <form
            action={async () => {
              "use server";
              await signOut({ redirectTo: "/login" });
            }}
            className="border-l border-[#555b61] pl-3"
          >
            <button className="cursor-pointer text-sm hover:underline">Sair</button>
          </form>
        </div>
      </header>

      <div className="flex min-w-0 flex-1 flex-col md:flex-row">
        <MenuLateral />
        <main className="min-w-0 flex-1 px-4 py-5 md:px-6">{children}</main>
      </div>
    </div>
  );
}

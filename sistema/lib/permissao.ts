import { redirect } from "next/navigation";
import { auth } from "@/auth";

// RNF02: a permissao e decidida aqui no servidor, nunca so escondendo botao na tela.
// toda pagina e toda action do administrador chamam essa funcao antes de fazer qualquer coisa
export async function exigirPerfil(perfil: "administrador" | "prestador" | "cliente") {
  const sessao = await auth();
  if (!sessao?.user) redirect("/login");
  if (sessao.user.perfil !== perfil) redirect("/sem-permissao");
  return sessao.user;
}

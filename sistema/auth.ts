import NextAuth, { CredentialsSignin } from "next-auth";
import Credentials from "next-auth/providers/credentials";
import { authConfig } from "./auth.config";
import { verificarLogin } from "@/lib/dominio/login";

class ContaBloqueada extends CredentialsSignin {
  code = "bloqueado";
}

export const { handlers, auth, signIn, signOut } = NextAuth({
  ...authConfig,
  providers: [
    Credentials({
      credentials: { email: {}, senha: {} },
      async authorize(credenciais) {
        const resultado = await verificarLogin(String(credenciais.email ?? ""), String(credenciais.senha ?? ""));
        if (resultado.ok) return resultado.usuario;
        if (resultado.motivo === "bloqueado") throw new ContaBloqueada();
        return null;
      },
    }),
  ],
});

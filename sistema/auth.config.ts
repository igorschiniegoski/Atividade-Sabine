import type { NextAuthConfig } from "next-auth";

// parte da configuracao que tambem roda no middleware. nao pode importar prisma nem bcrypt,
// porque o middleware do next roda fora do node. o provider de login fica no auth.ts
export const authConfig = {
  pages: { signIn: "/login" },
  // RNF03: a sessao expira com 30 minutos sem atividade. updateAge 0 renova o prazo a cada requisicao
  session: { strategy: "jwt", maxAge: 30 * 60, updateAge: 0 },
  providers: [],
  callbacks: {
    jwt({ token, user }) {
      if (user) {
        token.id = user.id;
        token.perfil = user.perfil;
      }
      return token;
    },
    session({ session, token }) {
      session.user.id = token.id as string;
      session.user.perfil = token.perfil as string;
      return session;
    },
  },
} satisfies NextAuthConfig;

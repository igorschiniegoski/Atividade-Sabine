import "next-auth";

// o perfil (administrador, prestador ou cliente) viaja dentro da sessao
declare module "next-auth" {
  interface User {
    perfil?: string;
  }
  interface Session {
    user: {
      id: string;
      name: string;
      email: string;
      perfil: string;
    };
  }
}

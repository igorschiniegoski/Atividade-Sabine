"use server";

import { AuthError, CredentialsSignin } from "next-auth";
import { signIn } from "@/auth";

export async function entrar(_estado: string | null, form: FormData) {
  try {
    await signIn("credentials", {
      email: form.get("email"),
      senha: form.get("senha"),
      redirectTo: "/prestadores",
    });
    return null;
  } catch (erro) {
    if (erro instanceof CredentialsSignin && erro.code === "bloqueado") {
      return "Muitas tentativas erradas para este e-mail. Tente de novo em 15 minutos.";
    }
    if (erro instanceof AuthError) {
      // mesma mensagem pra email e senha, sem dizer qual dos dois errou (UC01)
      return "E-mail ou senha inválidos.";
    }
    // o redirect do next tambem chega aqui como erro e precisa seguir adiante
    throw erro;
  }
}

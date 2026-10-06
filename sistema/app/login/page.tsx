"use client";

import { useActionState } from "react";
import { entrar } from "./actions";

// T01 - login
export default function Login() {
  const [estado, enviar, enviando] = useActionState(entrar, { erro: null, email: "" });
  const erro = estado.erro;

  return (
    <main className="flex min-h-screen items-center justify-center bg-caneta-escura px-4">
      <div className="w-full max-w-sm">
        <h1 className="text-3xl font-bold text-white">SGP</h1>
        <p className="mb-4 text-sm text-[#aab0b6]">Gestão de prestadores de serviço</p>

        <form action={enviar} className="cartao space-y-3 p-4">
          <div>
            <label htmlFor="email" className="rotulo">E-mail</label>
            <input id="email" name="email" type="email" required autoComplete="username" defaultValue={estado.email}
              className={`campo ${erro ? "campo-erro" : ""}`} />
          </div>
          <div>
            <label htmlFor="senha" className="rotulo">Senha</label>
            <input id="senha" name="senha" type="password" required autoComplete="current-password"
              className={`campo ${erro ? "campo-erro" : ""}`} />
            {erro && <p className="msg-erro" role="alert">{erro}</p>}
          </div>
          <button type="submit" disabled={enviando} className="botao-principal w-full">
            {enviando ? "Entrando..." : "Entrar"}
          </button>
        </form>
      </div>
    </main>
  );
}

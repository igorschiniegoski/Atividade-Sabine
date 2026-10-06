import bcrypt from "bcryptjs";
import { prisma } from "@/lib/db";

// RNF12: cinco erros seguidos no mesmo email bloqueiam novas tentativas por 15 minutos
export const LIMITE_TENTATIVAS = 5;
export const MINUTOS_BLOQUEIO = 15;

export function estaBloqueado(bloqueadoAte: Date | null, agora: Date) {
  return bloqueadoAte !== null && bloqueadoAte > agora;
}

// o que gravar no usuario depois de uma senha errada
export function registrarErro(tentativasAtuais: number, agora: Date) {
  const tentativas = tentativasAtuais + 1;
  if (tentativas >= LIMITE_TENTATIVAS) {
    return {
      tentativas_falhas: 0,
      bloqueado_ate: new Date(agora.getTime() + MINUTOS_BLOQUEIO * 60 * 1000),
    };
  }
  return { tentativas_falhas: tentativas, bloqueado_ate: null };
}

type Resultado =
  | { ok: true; usuario: { id: string; name: string; email: string; perfil: string } }
  | { ok: false; motivo: "invalido" | "bloqueado" };

export async function verificarLogin(email: string, senha: string): Promise<Resultado> {
  const agora = new Date();
  const usuario = await prisma.usuario.findUnique({ where: { email: email.trim().toLowerCase() } });

  // email que nao existe ou conta desativada recebem a mesma resposta de senha errada,
  // pra tela nao revelar qual dos dois esta errado (UC01)
  if (!usuario || !usuario.ativo) return { ok: false, motivo: "invalido" };

  if (estaBloqueado(usuario.bloqueado_ate, agora)) return { ok: false, motivo: "bloqueado" };

  const senhaConfere = await bcrypt.compare(senha, usuario.senha_hash);
  if (!senhaConfere) {
    const dados = registrarErro(usuario.tentativas_falhas, agora);
    await prisma.usuario.update({ where: { id_usuario: usuario.id_usuario }, data: dados });
    return { ok: false, motivo: dados.bloqueado_ate ? "bloqueado" : "invalido" };
  }

  await prisma.usuario.update({
    where: { id_usuario: usuario.id_usuario },
    data: { tentativas_falhas: 0, bloqueado_ate: null, ultimo_acesso_em: agora },
  });

  return {
    ok: true,
    usuario: { id: String(usuario.id_usuario), name: usuario.nome, email: usuario.email, perfil: usuario.perfil },
  };
}

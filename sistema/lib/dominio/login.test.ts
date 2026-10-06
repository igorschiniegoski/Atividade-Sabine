import { describe, expect, it } from "vitest";
import { estaBloqueado, registrarErro } from "./login";

const agora = new Date("2026-10-20T19:00:00");

describe("bloqueio por tentativas (RNF12)", () => {
  it("soma o erro sem bloquear ate a quarta tentativa", () => {
    expect(registrarErro(0, agora)).toEqual({ tentativas_falhas: 1, bloqueado_ate: null });
    expect(registrarErro(3, agora)).toEqual({ tentativas_falhas: 4, bloqueado_ate: null });
  });

  it("na quinta tentativa bloqueia por 15 minutos e zera a contagem", () => {
    const r = registrarErro(4, agora);
    expect(r.tentativas_falhas).toBe(0);
    expect(r.bloqueado_ate).toEqual(new Date("2026-10-20T19:15:00"));
  });

  it("considera bloqueado so enquanto o horario nao passou", () => {
    const ate = new Date("2026-10-20T19:15:00");
    expect(estaBloqueado(ate, agora)).toBe(true);
    expect(estaBloqueado(ate, new Date("2026-10-20T19:16:00"))).toBe(false);
    expect(estaBloqueado(null, agora)).toBe(false);
  });
});

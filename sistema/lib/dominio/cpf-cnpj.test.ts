import { describe, expect, it } from "vitest";
import { cnpjValido, cpfValido, documentoValido, formatarCpfCnpj } from "./cpf-cnpj";

describe("cpf", () => {
  it("aceita cpf valido com e sem mascara", () => {
    expect(cpfValido("529.982.247-25")).toBe(true);
    expect(cpfValido("52998224725")).toBe(true);
  });

  it("recusa digito verificador errado", () => {
    expect(cpfValido("529.982.247-26")).toBe(false);
  });

  it("recusa numeros repetidos e tamanho errado", () => {
    expect(cpfValido("111.111.111-11")).toBe(false);
    expect(cpfValido("5299822472")).toBe(false);
  });
});

describe("cnpj", () => {
  it("aceita cnpj valido", () => {
    expect(cnpjValido("11.222.333/0001-81")).toBe(true);
  });

  it("recusa digito verificador errado", () => {
    // mesmo caso da tela T04 do prototipo
    expect(cnpjValido("11.222.333/0001-00")).toBe(false);
  });

  it("recusa numeros repetidos", () => {
    expect(cnpjValido("00.000.000/0000-00")).toBe(false);
  });
});

describe("documento pelo tipo de pessoa", () => {
  it("usa cpf para F e cnpj para J", () => {
    expect(documentoValido("F", "52998224725")).toBe(true);
    expect(documentoValido("J", "52998224725")).toBe(false);
    expect(documentoValido("J", "11222333000181")).toBe(true);
  });

  it("formata para exibir", () => {
    expect(formatarCpfCnpj("52998224725")).toBe("529.982.247-25");
    expect(formatarCpfCnpj("11222333000181")).toBe("11.222.333/0001-81");
  });
});

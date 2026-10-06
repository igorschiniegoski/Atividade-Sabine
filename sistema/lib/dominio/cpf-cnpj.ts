// RN10: cpf e cnpj precisam ser validos pelo digito verificador.
// a unicidade (nao repetir cadastro) e conferida no banco, na hora de salvar.

export function soDigitos(valor: string) {
  return valor.replace(/\D/g, "");
}

export function cpfValido(valor: string) {
  const cpf = soDigitos(valor);
  if (cpf.length !== 11) return false;
  // 000.000.000-00, 111.111.111-11 etc passam na conta mas nao existem
  if (/^(\d)\1{10}$/.test(cpf)) return false;

  for (const tamanho of [9, 10]) {
    let soma = 0;
    for (let i = 0; i < tamanho; i++) {
      soma += Number(cpf[i]) * (tamanho + 1 - i);
    }
    let digito = (soma * 10) % 11;
    if (digito === 10) digito = 0;
    if (digito !== Number(cpf[tamanho])) return false;
  }
  return true;
}

export function cnpjValido(valor: string) {
  const cnpj = soDigitos(valor);
  if (cnpj.length !== 14) return false;
  if (/^(\d)\1{13}$/.test(cnpj)) return false;

  const pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2];
  const pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2];

  for (const pesos of [pesos1, pesos2]) {
    let soma = 0;
    for (let i = 0; i < pesos.length; i++) {
      soma += Number(cnpj[i]) * pesos[i];
    }
    const resto = soma % 11;
    const digito = resto < 2 ? 0 : 11 - resto;
    if (digito !== Number(cnpj[pesos.length])) return false;
  }
  return true;
}

// tipo F = pessoa fisica (cpf), J = juridica (cnpj)
export function documentoValido(tipo: string, valor: string) {
  return tipo === "F" ? cpfValido(valor) : cnpjValido(valor);
}

export function formatarCpfCnpj(valor: string) {
  const d = soDigitos(valor);
  if (d.length === 11) return d.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
  if (d.length === 14) return d.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, "$1.$2.$3/$4-$5");
  return valor;
}

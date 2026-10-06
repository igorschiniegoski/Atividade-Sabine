// carga inicial (docs/modelo-de-dados.md, secao 9) + prestadores ficticios para teste.
// todos os dados sao inventados, conforme a restricao de lgpd da 1a entrega.
// rodar com: npm run db:carga (pode rodar mais de uma vez, nao duplica)
import { PrismaClient } from "@prisma/client";
import bcrypt from "bcryptjs";

const prisma = new PrismaClient();

const SENHA_TESTE = "sgp@2026";

async function main() {
  const hash = await bcrypt.hash(SENHA_TESTE, 10); // RNF01, custo 10

  for (const adm of [
    { nome: "Luis Gustavo Boratto", email: "luis@sgp.teste" },
    { nome: "Igor Schiniegoski Pallisser", email: "igor@sgp.teste" },
  ]) {
    await prisma.usuario.upsert({
      where: { email: adm.email },
      update: {},
      create: { ...adm, senha_hash: hash, perfil: "administrador" },
    });
  }

  const tipos = [
    { nome: "CPF", obrigatorio: true, exige_validade: false },
    { nome: "RG", obrigatorio: true, exige_validade: false },
    { nome: "CNPJ", obrigatorio: true, exige_validade: false },
    { nome: "Certidão negativa de débitos", obrigatorio: true, exige_validade: true },
    { nome: "Comprovante de endereço", obrigatorio: false, exige_validade: false },
    { nome: "Apólice de seguro", obrigatorio: false, exige_validade: true },
    { nome: "Certificado de curso", obrigatorio: false, exige_validade: true },
  ];
  for (const tipo of tipos) {
    await prisma.tipo_documento.upsert({ where: { nome: tipo.nome }, update: {}, create: tipo });
  }

  for (const nome of ["Elétrica", "Hidráulica", "Limpeza", "Manutenção predial", "Refrigeração", "Informática"]) {
    await prisma.categoria_servico.upsert({ where: { nome }, update: {}, create: { nome } });
  }

  const endereco = { logradouro: "Avenida Brasil", bairro: "Centro", cidade: "Maringá", uf: "PR", cep: "87013000" };
  const prestadores = [
    { tipo_pessoa: "J", nome_razao_social: "ELETRICA SANTOS E CIA LTDA", nome_fantasia: "Elétrica Santos", cpf_cnpj: "07412865000104", telefone: "(44) 99812-4410", numero: "1420", situacao: "ativo" },
    { tipo_pessoa: "F", nome_razao_social: "JOSE CARLOS DE OLIVEIRA", cpf_cnpj: "04128837679", telefone: "(44) 99745-2201", numero: "88", situacao: "pendente" },
    { tipo_pessoa: "J", nome_razao_social: "LIMPADORA SAO JUDAS LTDA", nome_fantasia: "São Judas", cpf_cnpj: "19603774000135", telefone: "(44) 3025-7788", numero: "310", situacao: "ativo" },
    { tipo_pessoa: "J", nome_razao_social: "POLAR REFRIGERACAO E CLIMATIZACAO LTDA", nome_fantasia: "Polar", cpf_cnpj: "26155908000168", telefone: "(44) 99120-3377", numero: "57", situacao: "bloqueado" },
    { tipo_pessoa: "F", nome_razao_social: "VALDIR APARECIDO DA SILVA", cpf_cnpj: "88304152940", telefone: "(44) 99666-1180", numero: "1002", situacao: "pendente" },
    { tipo_pessoa: "J", nome_razao_social: "HIDRAULICA PONTO CERTO LTDA", nome_fantasia: "Ponto Certo", cpf_cnpj: "33810427000104", telefone: "(44) 3263-9021", numero: "45", situacao: "ativo" },
    { tipo_pessoa: "F", nome_razao_social: "MARCIA REGINA FERREIRA", cpf_cnpj: "31765290406", telefone: "(44) 99871-5530", numero: "230", situacao: "inativo" },
  ];
  for (const p of prestadores) {
    await prisma.prestador.upsert({
      where: { cpf_cnpj: p.cpf_cnpj },
      update: {},
      create: { ...endereco, ...p },
    });
  }

  console.log(`carga feita. login de teste: luis@sgp.teste ou igor@sgp.teste, senha ${SENHA_TESTE}`);
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(() => prisma.$disconnect());

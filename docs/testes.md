# sgp - sistema de gestao de prestadores
## casos de teste e registro de defeitos

**versao 1.0 - 06/10/2026 - 1ª entrega do 2º bimestre (20/10)**
unicesumar - analise e desenvolvimento de sistemas
imersao profissional - projeto de software - equipe 8

---

## 1. o que este documento registra

os testes do que ja foi implementado: login e cadastro e consulta de prestadores, que é o recorte escolhido pra entrega de 20/10 (ver [entrega-20-10.md](entrega-20-10.md)). é um documento vivo, a cada entrega entram os casos das funcionalidades novas e os que ja existem sao executados de novo.

tem dois tipos de teste:

| tipo | o que cobre | como roda |
|---|---|---|
| unitario (vitest) | as regras que ficam em `lib/dominio`: digito verificador do cpf e do cnpj (RN10) e a contagem do bloqueio de login (RNF12) | `npm test` dentro da pasta `sistema` |
| manual, no navegador | o uso de verdade pela tela, incluindo banco, sessao e mensagens | seguindo os passos de cada caso abaixo |

## 2. condicões de execucao

| item | valor |
|---|---|
| data | 06/10/2026 |
| versao testada | commit `1239a07` (casos CT01 a CT21). o reteste do defeito D01 foi no commit `87a0287` |
| ambiente | windows 11, node 22.14, google chrome, tela de 1280x800 e de 390x844 (celular) |
| como o ambiente foi montado | clone novo do repositorio numa pasta vazia, seguindo so o readme: `npm install`, `npm run banco`, `npm run db:migrar`, `npm run db:carga` e `npm run dev`. serviu tambem pra conferir que o passo a passo do readme funciona do zero |
| dados | os da carga inicial (`prisma/seed.ts`), todos ficticios. usuarios de teste `luis@sgp.teste` e `igor@sgp.teste`, senha `sgp@2026` |

## 3. testes unitarios

11 testes, todos passando. a saida completa do `npm test` esta em [evidencias/entrega-20-10/testes-unitarios.txt](evidencias/entrega-20-10/testes-unitarios.txt).

| arquivo | o que testa | testes |
|---|---|---|
| `lib/dominio/cpf-cnpj.test.ts` | cpf e cnpj validos com e sem mascara, digito errado, numero repetido (111.111.111-11), tamanho errado, escolha entre cpf e cnpj pelo tipo de pessoa e a formatacao pra tela | 8 |
| `lib/dominio/login.test.ts` | as quatro primeiras senhas erradas so somam, a quinta bloqueia por 15 minutos e zera a contagem, e o bloqueio acaba quando passa o horario | 3 |

## 4. casos de teste manuais

a coluna evidencia aponta pro print salvo em `docs/evidencias/entrega-20-10/`. caso sem print teve o resultado conferido na propria tela ou no banco, e o que apareceu esta descrito na coluna observado.

### 4.1 login e acesso (RF01, RNF02, RNF03, RNF12)

| caso | requisito | passos e entrada | esperado | observado | situacao | evidencia |
|---|---|---|---|---|---|---|
| CT01 | RF01 | entrar com `luis@sgp.teste` e a senha certa | abrir a lista de prestadores com o nome do usuario no topo | abriu `/prestadores`, cabecalho com "Luis Gustavo Boratto - Administrador" | passou | CT01-login-valido-lista-de-prestadores.png |
| CT02 | RF01 | mesmo email com a senha `senhaerrada` | ficar no login com "E-mail ou senha inválidos." e manter o email digitado | ficou no login com a mensagem e o email preenchido (depois da correcao do D01) | passou no reteste | CT02-senha-errada.png |
| CT03 | RF01, UC01 | email que nao existe, `naoexiste@sgp.teste` | a mesma mensagem do CT02, sem dizer que o email nao existe | mesma mensagem, "E-mail ou senha inválidos." | passou | - |
| CT04 | RNF12 | errar a senha do `igor@sgp.teste` 5 vezes seguidas e depois tentar com a senha certa | da 1ª a 4ª: senha invalida. na 5ª e na tentativa com a senha certa: aviso de bloqueio de 15 minutos | 1ª a 4ª "E-mail ou senha inválidos.", 5ª e 6ª "Muitas tentativas erradas para este e-mail. Tente de novo em 15 minutos.", sem entrar | passou no reteste | CT04-bloqueio-apos-cinco-erros.png |
| CT05 | RNF02 | sem estar logado, abrir direto `/prestadores/novo` | ser levado pro login | foi levado pra `/login` | passou | CT05-sem-login-volta-para-login.png |
| CT18 | RNF03 | depois do login, conferir o cookie de sessao no navegador | sessao valendo 30 minutos | cookie `authjs.session-token` vencendo 30 minutos depois do login. a renovacao a cada requisicao vem do `updateAge: 0` no `auth.config.ts` | passou | - |
| CT21 | RNF01 | consultar a tabela `usuario` no banco | senha gravada so como hash bcrypt | as duas senhas gravadas como `$2b$10$...`, 60 caracteres, nenhuma em texto puro | passou | - |

### 4.2 cadastro e consulta de prestadores (RF02, RN10, RNF04, RNF06)

| caso | requisito | passos e entrada | esperado | observado | situacao | evidencia |
|---|---|---|---|---|---|---|
| CT12 | RF02 | em novo prestador, clicar em salvar sem preencher nada | nao salvar e destacar os campos obrigatorios | nao salvou, 8 campos destacados e o aviso "Confira os campos destacados." | passou | CT12-campos-obrigatorios.png |
| CT09 | RN10 | pessoa juridica com cnpj `42.091.765/0001-00` (digito errado) e o resto preenchido | recusar no campo cnpj e manter o que ja foi digitado | "CNPJ inválido: o dígito verificador não confere." e a razao social continuou preenchida | passou | CT09-cnpj-digito-errado.png |
| CT07 | RF02 | o mesmo cadastro com o cnpj certo, `42.091.765/0001-24` | salvar, voltar pra lista com aviso e o prestador aparecer como pendente | voltou com "Prestador cadastrado. Ele entra como pendente até a documentação ser conferida." e a linha nova com situacao pendente | passou | CT07-cadastro-pj-valido.png |
| CT11 | RN10 | outro cadastro usando o mesmo cnpj `42091765000124`, sem mascara | recusar porque o cnpj ja existe | "Já existe um prestador cadastrado com este CNPJ." | passou | CT11-cnpj-repetido.png |
| CT10 | RN10 | pessoa fisica com cpf `562.190.837-00` (digito errado) | o rotulo do campo virar CPF e recusar o numero | rotulo "CPF" e a mensagem "CPF inválido: o dígito verificador não confere." | passou | CT10-cpf-digito-errado.png |
| CT08 | RF02 | o mesmo cadastro com o cpf certo, `562.190.837-68` | salvar | "Prestador cadastrado..." | passou | - |
| CT20 | RF02, RF09 | consultar a tabela `historico_situacao` depois do CT07 e do CT08 | cada cadastro novo ter o primeiro registro do historico | 2 registros: situacao anterior vazia, nova "pendente", motivo "cadastro inicial do prestador", feito pelo luis | passou | - |
| CT13 | RF02 | buscar por `eletrica` | trazer so os prestadores com esse nome | 2 encontrados: central eletrica zona sete e eletrica santos | passou | CT13-busca-por-nome.png |
| CT14 | RF02 | buscar pelo cnpj com mascara `07.412.865/0001-04` | achar o prestador mesmo com ponto, barra e traco | trouxe so a eletrica santos | passou | - |
| CT15 | RF02 | filtrar a situacao pendente | listar so pendentes | 4 linhas, todas pendentes | passou | CT15-filtro-pendente.png |
| CT16 | RF02 | abrir o prestador do CT07, trocar o telefone pra `(44) 3031-2020` e salvar | salvar e mostrar o telefone novo na lista | "Alterações salvas." e a linha com o telefone novo | passou | CT16-edicao-salva.png |
| CT17 | RF02 | desligar o banco (`ctrl+c` no `npm run banco`) e o sistema, ligar os dois de novo e buscar `zona` | o prestador do CT07 continuar la, com o telefone do CT16 | continuou, com o telefone (44) 3031-2020 | passou | CT17-dados-continuam-apos-reiniciar.png |
| CT19 | RNF04 | abrir o cadastro numa tela de 390 px de largura | nenhuma rolagem horizontal, campos um embaixo do outro | conteudo com 375 px dentro dos 390, campos empilhados | passou | CT19-celular-390px.png |

**resumo:** 21 casos manuais executados, 21 passaram (o CT02 e o CT04 depois do reteste do D01). 11 testes unitarios passando.

## 5. defeitos encontrados

| id | onde apareceu | como reproduzir | esperado | observado | situacao | correcao |
|---|---|---|---|---|---|---|
| D01 | print do CT04 | errar a senha no login | o email digitado continuar no campo | o campo de email voltava vazio. o react 19 limpa o formulario depois da action | corrigido e retestado (CT02 e CT04 passaram) | commit `87a0287`. a action do login devolve o email junto com a mensagem |
| D02 | conferencia visual do formulario, antes do commit da entrega | abrir o cadastro numa tela de uns 930 px | campos legiveis, sem barra de rolagem | o campo tipo cortava "Pessoa jurídica" e a linha das abas ganhava barra de rolagem | corrigido antes do commit `1239a07` | grade do formulario refeita em 12 colunas e abas quebrando linha |
| D03 | conferencia no celular, antes do commit da entrega | abrir qualquer tela com 390 px | o menu mostrar prestadores logo de cara | o menu horizontal comecava pelos itens em desenvolvimento e prestadores ficava escondido na rolagem | corrigido antes do commit `1239a07` | no celular os itens em desenvolvimento ficam ocultos |
| D04 | conferencia da tela de edicao, antes do commit da entrega | abrir um prestador ja cadastrado | cep no formato 00000-000 | aparecia so os 8 numeros | corrigido antes do commit `1239a07` | a tela formata o cep ao carregar |

nenhum defeito aberto nesta versao.

## 6. o que ainda nao foi testado

| item | por que | quando |
|---|---|---|
| RNF06, listagem em ate 3 segundos com 5 mil prestadores | a paginacao ja é feita no banco, de 20 em 20, mas falta a carga de 5 mil registros pra medir | 06/11, junto com o script de carga grande |
| acesso dos perfis prestador e cliente | as telas desses perfis ainda nao existem. hoje um usuario desses cai na tela "Acesso não liberado" | quando as telas T13 a T18 forem feitas |
| chamada da action de salvar sem sessao, montada fora da tela | a action chama `exigirPerfil` antes de tudo (ver `app/(admin)/prestadores/actions.ts`), mas falta um teste automatizado que prove isso | 06/11 |

---

## historico de alteracões

| versao | data | alteracao |
|---|---|---|
| 1.0 | 06/10/2026 | primeira versao, com os testes do recorte da 1ª entrega do 2º bimestre |

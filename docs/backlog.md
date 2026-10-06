# sgp - sistema de gestao de prestadores
## backlog e quadro de tarefas

**versao 1.1 - 06/10/2026 - 1ª entrega do 2º bimestre (20/10)**
unicesumar - analise e desenvolvimento de sistemas
imersao profissional - projeto de software - equipe 8

---

## 1. como o quadro funciona

este é o documento vivo do projeto: a cada trabalho concluido a linha correspondente muda de situacao. os demais documentos descrevem o sistema, este descreve o andamento da equipe.

| campo | o que registra |
|---|---|
| id | identificador da tarefa, no formato TA00 |
| tarefa | o que precisa ser feito, em uma frase |
| requisito | o RF, a historia ou o item de entrega que originou a tarefa |
| prioridade | alta, media ou baixa, herdada da priorizacao moscow da 2ª entrega |
| responsavel | quem conduz. o outro integrante revisa |
| prazo | a entrega em que a tarefa precisa estar pronta: 20/10, 06/11 ou 27/11. tarefa ja concluida mostra a data em que terminou |
| situacao | a fazer, em andamento ou concluida |

as tarefas de prioridade **alta** sao as que compõem o mvp. media sao os complementos da release 4, e baixa é o que ficou no backlog.

a partir do 2º bimestre a situacao de cada tarefa tambem fica registrada no git: o commit que fecha a tarefa cita o id dela na mensagem, por exemplo `feat: cadastro, edicao e consulta de prestadores (TA22)`.

### 1.1 quem faz o que

a divisao nao significa que cada integrante conhece apenas a propria parte. as tarefas sao conduzidas por um e revisadas pelo outro, e os dois precisam saber explicar o projeto inteiro.

| integrante | frente principal |
|---|---|
| luis gustavo boratto de oliveira | modelagem de dados, backend, regras de negocio e o fluxo da ordem de servico |
| igor schiniegoski pallisser | requisitos, casos de uso, interface, prototipo e a documentacao das entregas |

---

## 2. o que ja foi concluido

| id | tarefa | requisito | prioridade | responsavel | prazo | situacao |
|---|---|---|---|---|---|---|
| TA01 | levantar o problema, o escopo e os 19 requisitos funcionais | 1ª entrega | alta | igor | 14/08 | concluida |
| TA02 | definir os requisitos nao funcionais e as 12 regras de negocio | 1ª entrega | alta | luis | 14/08 | concluida |
| TA03 | modelar os 24 casos de uso e os cinco diagramas de caso de uso | 2ª entrega | alta | igor | 08/09 | concluida |
| TA04 | escrever as 23 historias de usuario com criterios de aceite | 2ª entrega | alta | igor | 08/09 | concluida |
| TA05 | priorizar o escopo com a escala moscow | 2ª entrega | alta | luis | 08/09 | concluida |
| TA06 | definir a stack e a arquitetura em camadas | 2ª entrega | alta | luis | 08/09 | concluida |
| TA07 | desenhar os diagramas de atividade de UC13 e UC16 | 2ª entrega | alta | luis | 08/09 | concluida |
| TA08 | montar o diagrama de classes do dominio | 2ª entrega | alta | luis | 08/09 | concluida |
| TA09 | modelar o banco: conceitual, logico e dicionario de dados | 2ª entrega | alta | luis | 08/09 | concluida |
| TA10 | desenhar o diagrama de arquitetura | 2ª entrega | alta | luis | 08/09 | concluida |
| TA11 | definir o mvp e o fluxo completo do sistema | 3ª entrega | alta | luis | 25/09 | concluida |
| TA12 | levantar as telas do mvp e montar o mapa de navegacao | 3ª entrega | alta | igor | 25/09 | concluida |
| TA13 | construir o prototipo navegavel das 18 telas | 3ª entrega | alta | igor | 25/09 | concluida |
| TA14 | organizar o repositorio, o readme e o gitignore | 3ª entrega | media | luis | 25/09 | concluida |
| TA15 | preparar o roteiro da apresentacao | 3ª entrega | alta | igor | 25/09 | concluida |

---

## 3. release 1 - base do sistema

autenticacao e cadastros de apoio. sem esta release nao ha o que atribuir.

| id | tarefa | requisito | prioridade | responsavel | prazo | situacao |
|---|---|---|---|---|---|---|
| TA16 | criar o projeto next.js, configurar o prisma e publicar o primeiro deploy na vercel. projeto e prisma prontos, falta o deploy | RNF08, RNF11 | alta | luis | 06/11 | em andamento |
| TA17 | escrever as migracões das 14 tabelas do modelo logico | modelo de dados | alta | luis | 20/10 | concluida |
| TA18 | implementar o login com hash bcrypt, sessao de 30 minutos e bloqueio apos cinco tentativas | RF01, HU01, HU02, RNF12 | alta | luis | 20/10 | concluida |
| TA19 | implementar a autorizacao por perfil nas rotas de api | RNF02 | alta | luis | 20/10 | concluida |
| TA20 | montar o layout base: cabecalho, menu por perfil e componentes de tabela e formulario | RNF04 | alta | luis | 20/10 | concluida |
| TA21 | construir a tela de login (T01) | RF01 | alta | luis | 20/10 | concluida |
| TA22 | construir o cadastro e a listagem de prestadores (T03 e T04) | RF02, HU03 | alta | luis | 20/10 | concluida |
| TA23 | implementar a validacao de cpf e cnpj com digito verificador e unicidade | RN10 | alta | luis | 20/10 | concluida |
| TA24 | construir o cadastro e a listagem de clientes (T05 e T06) | RF03, HU04 | alta | igor | 06/11 | a fazer |
| TA25 | construir as categorias de servico (T07) | RF04, HU05 | alta | igor | 06/11 | a fazer |
| TA26 | construir o catalogo de servicos (T08 e T09) | RF05, HU06 | alta | igor | 06/11 | a fazer |
| TA27 | implementar a habilitacao do prestador por categoria (T04) | RF06, HU07, RN04 | alta | luis | 06/11 | a fazer |
| TA58 | rodar o sistema do zero na maquina do igor seguindo so o readme, e corrigir o readme no que faltar | RNF11, manual da entrega | alta | igor | 20/10 | a fazer |
| TA59 | escrever e executar os casos de teste do recorte, com evidencias | manual da entrega | alta | luis | 20/10 | concluida |
| TA60 | registrar a revisao do 1º bimestre e atualizar tecnologias, modelo de dados e rastreabilidade | manual da entrega | alta | luis | 20/10 | concluida |
| TA61 | gerar 5 mil prestadores ficticios e medir o tempo da listagem | RNF06 | alta | luis | 06/11 | a fazer |
| TA62 | teste automatizado provando que a action de salvar recusa chamada sem sessao ou com outro perfil | RNF02 | alta | luis | 06/11 | a fazer |

### 3.1 quando uma tarefa do recorte esta concluida

criterios verificaveis das tarefas que fazem parte da entrega de 20/10. sao eles que viraram os casos de teste do [testes.md](testes.md).

| tarefa | concluida quando | casos de teste |
|---|---|---|
| TA17 | `npm run db:migrar` cria as 14 tabelas num banco vazio, com os check do dicionario de dados | clone novo, testes.md secao 2 |
| TA18 | login certo entra, errado mostra a mesma mensagem pra email e senha, a 5ª senha errada seguida bloqueia por 15 minutos, a senha so existe em hash e a sessao vence em 30 minutos | CT01 a CT04, CT18, CT21 |
| TA19 | nenhuma tela ou action do administrador funciona sem login ou com outro perfil | CT05 |
| TA20 | cabecalho com usuario e sair, menu com o que existe e o que esta em desenvolvimento, sem rolagem horizontal no celular | CT01, CT19 |
| TA21 | tela de login igual a T01 do prototipo, com a mensagem de erro e sem perder o email digitado | CT02, CT04 |
| TA22 | dados validos sao salvos, obrigatorio vazio é recusado com o campo destacado, o cadastro aparece na consulta, a edicao salva e os dados continuam depois de reiniciar | CT07, CT08, CT12 a CT17 |
| TA23 | cpf e cnpj com digito errado sao recusados com a mensagem no campo, e documento repetido nao é aceito | unitarios, CT09 a CT11 |

## 4. release 2 - documentacao e situacao cadastral

o que diferencia o sistema da planilha.

| id | tarefa | requisito | prioridade | responsavel | prazo | situacao |
|---|---|---|---|---|---|---|
| TA28 | configurar o storage de arquivos e o upload com limite de 10 mb | RNF09 | alta | luis | 06/11 | a fazer |
| TA29 | construir o envio de documentos pelo prestador (T15) | RF07, HU08 | alta | igor | 06/11 | a fazer |
| TA30 | implementar o versionamento do documento, mantendo a versao anterior no historico | HU08 | alta | luis | 06/11 | a fazer |
| TA31 | construir o painel de vencimentos (T10) | RF08, HU09 | alta | igor | 06/11 | a fazer |
| TA32 | implementar a rotina que muda a situacao para pendente quando um documento obrigatorio vence | RN02 | alta | luis | 06/11 | a fazer |
| TA33 | construir a alteracao de situacao cadastral com motivo e historico (T04) | RF09, HU11 | alta | igor | 06/11 | a fazer |
| TA34 | implementar a verificacao de aptidao do prestador, concentrando RN01 a RN04 | RF12, UC22 | alta | luis | 06/11 | a fazer |
| TA35 | impedir a inativacao de prestador com ordem em andamento | RN11 | alta | luis | 06/11 | a fazer |

## 5. release 3 - operacao, fim do mvp

o fluxo completo da ordem de servico.

| id | tarefa | requisito | prioridade | responsavel | prazo | situacao |
|---|---|---|---|---|---|---|
| TA36 | construir a abertura da solicitacao pelo cliente (T17) | RF11, HU12 | alta | igor | 27/11 | a fazer |
| TA37 | implementar a numeracao da ordem e o calculo do prazo pelo prazo padrao do servico | RF11 | alta | luis | 27/11 | a fazer |
| TA38 | construir a listagem de ordens com filtro (T11 e T16) | RF13, RF16 | alta | igor | 27/11 | a fazer |
| TA39 | construir a tela da ordem na visao do administrador (T12) | RF13 | alta | igor | 27/11 | a fazer |
| TA40 | implementar a atribuicao em transacao, revalidando a aptidao no servidor | RF12, HU13 | alta | luis | 27/11 | a fazer |
| TA41 | construir a selecao de prestador apto, com o motivo de cada inapto (T12) | RF12, HU13 | alta | igor | 27/11 | a fazer |
| TA42 | implementar a maquina de estado da ordem, recusando transicao fora da sequencia | RN05, RN06 | alta | luis | 27/11 | a fazer |
| TA43 | construir a execucao e a conclusao da ordem pelo prestador (T13 e T14) | RF13, RF14, HU15, HU16 | alta | igor | 27/11 | a fazer |
| TA44 | implementar o calculo de entrega no prazo ou em atraso na conclusao | RN12 | alta | luis | 27/11 | a fazer |
| TA45 | construir o cancelamento com motivo minimo de 10 caracteres (T12) | RF13, HU17, RN07 | alta | igor | 27/11 | a fazer |
| TA46 | construir a avaliacao do atendimento pelo cliente (T18) | RF15, HU18 | alta | igor | 27/11 | a fazer |
| TA47 | implementar a regra de avaliacao unica pelo cliente titular e o calculo da nota media | RN08, RN09 | alta | luis | 27/11 | a fazer |
| TA48 | escrever os testes das regras de negocio criticas e do fluxo completo | RNF02, RNF11 | alta | luis | 27/11 | a fazer |

## 6. release 4 - complementos

entram depois que todo o mvp estiver concluido e testado.

| id | tarefa | requisito | prioridade | responsavel | prazo | situacao |
|---|---|---|---|---|---|---|
| TA49 | implementar o log de acões criticas | RF19, HU22 | media | luis | depois do mvp | a fazer |
| TA50 | construir o cadastro de contratos com vigencia e anexo | RF10, HU10 | media | igor | depois do mvp | a fazer |
| TA51 | ativar a RN03 na verificacao de aptidao, agora que o contrato existe | RN03 | media | luis | depois do mvp | a fazer |
| TA52 | construir o aceite ou recusa da atribuicao pelo prestador | RF13, HU14 | media | igor | depois do mvp | a fazer |
| TA53 | construir o historico consolidado por prestador e por cliente | RF16, HU19 | media | igor | depois do mvp | a fazer |
| TA54 | construir o relatorio de desempenho do prestador | RF17, HU20 | media | luis | depois do mvp | a fazer |

## 7. backlog

reconhecido como pertinente, sem data definida.

| id | tarefa | requisito | prioridade | responsavel | prazo | situacao |
|---|---|---|---|---|---|---|
| TA55 | construir o relatorio de servicos por periodo | RF18, HU21 | baixa | a definir | sem data | a fazer |
| TA56 | implementar a exportacao de relatorio em pdf e csv | HU23 | baixa | a definir | sem data | a fazer |
| TA57 | implementar a anonimizacao de dados pessoais mediante solicitacao | RNF10 | baixa | luis | sem data | a fazer |

---

## 8. resumo

| situacao | tarefas |
|---|---|
| concluidas | 24 |
| em andamento | 1 (TA16, falta o deploy) |
| a fazer ate 20/10 | 1 (TA58, o readme na maquina do igor) |
| a fazer ate 06/11 | 14 |
| a fazer ate 27/11 | 13 |
| a fazer depois do mvp e backlog | 9 |
| **total** | **62** |

| responsavel | tarefas atribuidas |
|---|---|
| luis gustavo boratto de oliveira | 37 |
| igor schiniegoski pallisser | 23 |
| a definir | 2 |
| ambos, em revisao cruzada | todas |

---

## historico de alteracões

| versao | data | alteracao |
|---|---|---|
| 1.0 | 22/09/2026 | primeira versao do quadro de tarefas, com as 15 tarefas ja concluidas e as 42 planejadas |
| 1.1 | 06/10/2026 | coluna de prazo, criterios de conclusao do recorte de 20/10, TA17 a TA23 concluidas. TA20 a TA22 foram feitas junto com o backend pra fechar o recorte, e o igor assumiu TA24 a TA26 pra 06/11. entraram TA58 a TA62 |

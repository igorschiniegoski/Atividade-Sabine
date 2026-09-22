# sgp - sistema de gestao de prestadores
## backlog e quadro de tarefas

**versao 1.0 - 22/09/2026 - 3ª entrega**
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
| situacao | a fazer, em andamento ou concluida |

as tarefas de prioridade **alta** sao as que compõem o mvp. media sao os complementos da release 4, e baixa é o que ficou no backlog.

### 1.1 quem faz o que

a divisao nao significa que cada integrante conhece apenas a propria parte. as tarefas sao conduzidas por um e revisadas pelo outro, e os dois precisam saber explicar o projeto inteiro.

| integrante | frente principal |
|---|---|
| luis gustavo boratto de oliveira | modelagem de dados, backend, regras de negocio e o fluxo da ordem de servico |
| igor schiniegoski pallisser | requisitos, casos de uso, interface, prototipo e a documentacao das entregas |

---

## 2. o que ja foi concluido

| id | tarefa | requisito | prioridade | responsavel | situacao |
|---|---|---|---|---|---|
| TA01 | levantar o problema, o escopo e os 19 requisitos funcionais | 1ª entrega | alta | igor | concluida |
| TA02 | definir os requisitos nao funcionais e as 12 regras de negocio | 1ª entrega | alta | luis | concluida |
| TA03 | modelar os 24 casos de uso e os cinco diagramas de caso de uso | 2ª entrega | alta | igor | concluida |
| TA04 | escrever as 23 historias de usuario com criterios de aceite | 2ª entrega | alta | igor | concluida |
| TA05 | priorizar o escopo com a escala moscow | 2ª entrega | alta | luis | concluida |
| TA06 | definir a stack e a arquitetura em camadas | 2ª entrega | alta | luis | concluida |
| TA07 | desenhar os diagramas de atividade de UC13 e UC16 | 2ª entrega | alta | luis | concluida |
| TA08 | montar o diagrama de classes do dominio | 2ª entrega | alta | luis | concluida |
| TA09 | modelar o banco: conceitual, logico e dicionario de dados | 2ª entrega | alta | luis | concluida |
| TA10 | desenhar o diagrama de arquitetura | 2ª entrega | alta | luis | concluida |
| TA11 | definir o mvp e o fluxo completo do sistema | 3ª entrega | alta | luis | concluida |
| TA12 | levantar as telas do mvp e montar o mapa de navegacao | 3ª entrega | alta | igor | concluida |
| TA13 | construir o prototipo navegavel das 18 telas | 3ª entrega | alta | igor | concluida |
| TA14 | organizar o repositorio, o readme e o gitignore | 3ª entrega | media | luis | concluida |
| TA15 | preparar o roteiro da apresentacao | 3ª entrega | alta | igor | concluida |

---

## 3. release 1 - base do sistema

autenticacao e cadastros de apoio. sem esta release nao ha o que atribuir.

| id | tarefa | requisito | prioridade | responsavel | situacao |
|---|---|---|---|---|---|
| TA16 | criar o projeto next.js, configurar o prisma e publicar o primeiro deploy na vercel | RNF08, RNF11 | alta | luis | a fazer |
| TA17 | escrever as migracões das 14 tabelas do modelo logico | modelo de dados | alta | luis | a fazer |
| TA18 | implementar o login com hash bcrypt, sessao de 30 minutos e bloqueio apos cinco tentativas | RF01, HU01, HU02, RNF12 | alta | luis | a fazer |
| TA19 | implementar a autorizacao por perfil nas rotas de api | RNF02 | alta | luis | a fazer |
| TA20 | montar o layout base: cabecalho, menu por perfil e componentes de tabela e formulario | RNF04 | alta | igor | a fazer |
| TA21 | construir a tela de login (T01) | RF01 | alta | igor | a fazer |
| TA22 | construir o cadastro e a listagem de prestadores (T03 e T04) | RF02, HU03 | alta | igor | a fazer |
| TA23 | implementar a validacao de cpf e cnpj com digito verificador e unicidade | RN10 | alta | luis | a fazer |
| TA24 | construir o cadastro e a listagem de clientes (T05 e T06) | RF03, HU04 | alta | igor | a fazer |
| TA25 | construir as categorias de servico (T07) | RF04, HU05 | alta | igor | a fazer |
| TA26 | construir o catalogo de servicos (T08 e T09) | RF05, HU06 | alta | igor | a fazer |
| TA27 | implementar a habilitacao do prestador por categoria (T04) | RF06, HU07, RN04 | alta | luis | a fazer |

## 4. release 2 - documentacao e situacao cadastral

o que diferencia o sistema da planilha.

| id | tarefa | requisito | prioridade | responsavel | situacao |
|---|---|---|---|---|---|
| TA28 | configurar o storage de arquivos e o upload com limite de 10 mb | RNF09 | alta | luis | a fazer |
| TA29 | construir o envio de documentos pelo prestador (T15) | RF07, HU08 | alta | igor | a fazer |
| TA30 | implementar o versionamento do documento, mantendo a versao anterior no historico | HU08 | alta | luis | a fazer |
| TA31 | construir o painel de vencimentos (T10) | RF08, HU09 | alta | igor | a fazer |
| TA32 | implementar a rotina que muda a situacao para pendente quando um documento obrigatorio vence | RN02 | alta | luis | a fazer |
| TA33 | construir a alteracao de situacao cadastral com motivo e historico (T04) | RF09, HU11 | alta | igor | a fazer |
| TA34 | implementar a verificacao de aptidao do prestador, concentrando RN01 a RN04 | RF12, UC22 | alta | luis | a fazer |
| TA35 | impedir a inativacao de prestador com ordem em andamento | RN11 | alta | luis | a fazer |

## 5. release 3 - operacao, fim do mvp

o fluxo completo da ordem de servico.

| id | tarefa | requisito | prioridade | responsavel | situacao |
|---|---|---|---|---|---|
| TA36 | construir a abertura da solicitacao pelo cliente (T17) | RF11, HU12 | alta | igor | a fazer |
| TA37 | implementar a numeracao da ordem e o calculo do prazo pelo prazo padrao do servico | RF11 | alta | luis | a fazer |
| TA38 | construir a listagem de ordens com filtro (T11 e T16) | RF13, RF16 | alta | igor | a fazer |
| TA39 | construir a tela da ordem na visao do administrador (T12) | RF13 | alta | igor | a fazer |
| TA40 | implementar a atribuicao em transacao, revalidando a aptidao no servidor | RF12, HU13 | alta | luis | a fazer |
| TA41 | construir a selecao de prestador apto, com o motivo de cada inapto (T12) | RF12, HU13 | alta | igor | a fazer |
| TA42 | implementar a maquina de estado da ordem, recusando transicao fora da sequencia | RN05, RN06 | alta | luis | a fazer |
| TA43 | construir a execucao e a conclusao da ordem pelo prestador (T13 e T14) | RF13, RF14, HU15, HU16 | alta | igor | a fazer |
| TA44 | implementar o calculo de entrega no prazo ou em atraso na conclusao | RN12 | alta | luis | a fazer |
| TA45 | construir o cancelamento com motivo minimo de 10 caracteres (T12) | RF13, HU17, RN07 | alta | igor | a fazer |
| TA46 | construir a avaliacao do atendimento pelo cliente (T18) | RF15, HU18 | alta | igor | a fazer |
| TA47 | implementar a regra de avaliacao unica pelo cliente titular e o calculo da nota media | RN08, RN09 | alta | luis | a fazer |
| TA48 | escrever os testes das regras de negocio criticas e do fluxo completo | RNF02, RNF11 | alta | luis | a fazer |

## 6. release 4 - complementos

entram depois que todo o mvp estiver concluido e testado.

| id | tarefa | requisito | prioridade | responsavel | situacao |
|---|---|---|---|---|---|
| TA49 | implementar o log de acões criticas | RF19, HU22 | media | luis | a fazer |
| TA50 | construir o cadastro de contratos com vigencia e anexo | RF10, HU10 | media | igor | a fazer |
| TA51 | ativar a RN03 na verificacao de aptidao, agora que o contrato existe | RN03 | media | luis | a fazer |
| TA52 | construir o aceite ou recusa da atribuicao pelo prestador | RF13, HU14 | media | igor | a fazer |
| TA53 | construir o historico consolidado por prestador e por cliente | RF16, HU19 | media | igor | a fazer |
| TA54 | construir o relatorio de desempenho do prestador | RF17, HU20 | media | luis | a fazer |

## 7. backlog

reconhecido como pertinente, sem data definida.

| id | tarefa | requisito | prioridade | responsavel | situacao |
|---|---|---|---|---|---|
| TA55 | construir o relatorio de servicos por periodo | RF18, HU21 | baixa | a definir | a fazer |
| TA56 | implementar a exportacao de relatorio em pdf e csv | HU23 | baixa | a definir | a fazer |
| TA57 | implementar a anonimizacao de dados pessoais mediante solicitacao | RNF10 | baixa | luis | a fazer |

---

## 8. resumo

| situacao | tarefas |
|---|---|
| concluidas | 15 |
| a fazer, prioridade alta (mvp) | 33 |
| a fazer, prioridade media (release 4) | 6 |
| a fazer, prioridade baixa (backlog) | 3 |
| **total** | **57** |

| responsavel | tarefas atribuidas |
|---|---|
| luis gustavo boratto de oliveira | 27 |
| igor schiniegoski pallisser | 26 |
| a definir | 2 |
| ambos, em revisao cruzada | todas |

---

## historico de alteracões

| versao | data | alteracao |
|---|---|---|
| 1.0 | 22/09/2026 | primeira versao do quadro de tarefas, com as 15 tarefas ja concluidas e as 42 planejadas |

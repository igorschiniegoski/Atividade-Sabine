# sgp - sistema de gestao de prestadores

plataforma web pra controlar prestadores de servico terceirizados: cadastro, documentacao, contratos e o acompanhamento das ordens de servico do pedido ate a conclusao.

trabalho da disciplina de projeto de software (imersao profissional) - unicesumar, ads.
equipe 8 - 1º bimestre de 2026.

## equipe

| integrante | github |
|---|---|
| luis gustavo boratto de oliveira | [@Tox1469](https://github.com/Tox1469) |
| igor schiniegoski pallisser | [@igorschiniegoski](https://github.com/igorschiniegoski) |

## o problema

empresa de pequeno e medio porte quase nunca executa tudo com equipe propria, ela aciona uma rede de prestadores terceirizados conforme a demanda. só que esse controle costuma ficar fora de qualquer sistema: o cadastro em uma planilha, os documentos espalhados no drive e no email, o contrato impresso na gaveta e a distribuicao dos servicos acontecendo em grupo de whatsapp.

o resultado é sempre o mesmo. documento vence e ninguem percebe até a fiscalizacao chegar, servico é esquecido ou cobrado duas vezes, e a escolha de quem chamar continua sendo no "fulano é bom", porque não existe historico nenhum pra consultar.

## objetivo

centralizar em um sistema só o cadastro, a documentacao e a execucao dos servicos terceirizados, com controle de validade dos documentos, atribuicao das ordens pra prestadores que estejam realmente aptos, e historico de avaliacao pra apoiar a decisao de quem contratar da proxima vez.

## principais funcionalidades

- cadastro de prestadores, clientes e categorias de servico
- upload de documentos com data de validade e painel dos que estao vencendo
- contratos com vigencia e arquivo anexo
- situacao cadastral do prestador (ativo, pendente, bloqueado, inativo)
- abertura, atribuicao e acompanhamento das ordens de servico por status
- avaliacao do atendimento pelo cliente e historico por prestador
- relatorios de desempenho e de servicos por periodo

sao 3 perfis de acesso: administrador, prestador e cliente. cada um enxerga só o que é da responsabilidade dele.

a lista completa (19 requisitos funcionais, 11 nao funcionais e 12 regras de negocio) esta em [docs/documento-visao-requisitos.md](docs/documento-visao-requisitos.md).

## tecnologias previstas

| camada | escolha |
|---|---|
| interface | next.js + react |
| servidor | node.js (rotas de api do proprio next) |
| banco | postgresql |
| arquivos | storage em nuvem pros documentos e contratos |
| hospedagem | vercel |

a escolha foi por familiaridade da equipe e por serem ferramentas com plano gratuito, que é o que cabe no prazo e no orcamento do trabalho. nada disso esta fechado ainda, pode mudar até a 3ª entrega.

## organizacao do repositorio

```
docs/        documento de visao e requisitos
diagramas/   casos de uso, atividades e arquitetura (2ª entrega)
banco-de-dados/  modelo conceitual, logico e dicionario (2ª entrega)
prototipos/  mapa de navegacao e telas (3ª entrega)
src/         codigo fonte
```

as pastas vao sendo criadas conforme cada entrega. hoje só existe a docs/.

## entregas

| entrega | data | conteudo | status |
|---|---|---|---|
| 1 | 14/08/2026 | documento de visao e requisitos | pronto |
| 2 | 08/09/2026 | casos de uso, diagrama de classes e modelagem do banco | a fazer |
| 3 | 25/09/2026 | repositorio, prototipos e definicao do mvp | a fazer |

## como rodar

ainda não tem codigo. as instrucões de instalacao entram aqui quando a implementacao comecar, na 3ª entrega.

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

a lista completa (19 requisitos funcionais, 11 nao funcionais e 12 regras de negocio) esta em [docs/documento-visao-requisitos.md](docs/documento-visao-requisitos.md), e o desdobramento disso em casos de uso, historias de usuario e prioridades esta em [docs/casos-de-uso.md](docs/casos-de-uso.md).

## priorizacao

o escopo foi priorizado na **escala moscow**, que tem quatro niveis: **M**ust have, **S**hould have, **C**ould have e **W**ont have. a escolha foi por o prazo ser fixo e a equipe ter duas pessoas, entao o que precisa ser negociado é o escopo e nao a data.

| nivel | quantos | o que entrou |
|---|---|---|
| **M** - must have | 16 casos de uso | autenticacao, cadastros, documentacao, situacao cadastral e o fluxo completo da ordem de servico ate a avaliacao. é o mvp |
| **S** - should have | 5 casos de uso | contratos, aceite da atribuicao pelo prestador, historico consolidado, relatorio de desempenho e log |
| **C** - could have | 2 casos de uso | relatorio de servicos por periodo e exportacao em pdf ou csv |
| **W** - wont have | 8 itens | pagamento online, nota fiscal, assinatura digital, app nativo, whatsapp, aviso automatico por email, geolocalizacao e integracao com erp |

a definicao de cada nivel, o criterio de decisao e a justificativa item a item estao na secao 6 do [documento de casos de uso](docs/casos-de-uso.md).

## tecnologias previstas

| camada | escolha | por que |
|---|---|---|
| linguagem | typescript 5 | tipagem compartilhada entre tela e api |
| interface | next.js 15 (app router) + react 19 | um projeto so entrega tela e api |
| estilo | tailwind css + shadcn/ui | componentes responsivos prontos (RNF04) |
| servidor | node.js 20 lts, rotas de api do proprio next | menos configuracao e um deploy so |
| acesso a dados | prisma orm | migracões versionadas e schema como documentacao do modelo |
| banco | postgresql 16 | restricao de unicidade nativa pra RN10 e tipos de data adequados |
| autenticacao | auth.js v5 (credentials) + bcrypt | login por email e senha, sessao de 30 min (RF01, RNF01, RNF03) |
| validacao | zod | o mesmo esquema valida no formulario e na api (RNF02) |
| arquivos | storage de objetos em nuvem | documentos e contratos em pdf, jpg e png, ate 10 mb (RNF09) |
| hospedagem | vercel | url publica e deploy a cada push |
| testes | vitest e playwright | regras de negocio e fluxos criticos |

a escolha foi por familiaridade da equipe e por serem ferramentas com plano gratuito, que é o que cabe no prazo e no orcamento do trabalho. o detalhamento de cada decisao, as alternativas descartadas e a arquitetura em camadas estao em [docs/tecnologias-e-arquitetura.md](docs/tecnologias-e-arquitetura.md). continua em aberto apenas o provedor do postgresql gerenciado e do storage.

## organizacao do repositorio

```
docs/        documentos das entregas, do levantamento de requisitos ao roteiro da apresentacao
diagramas/   fontes .puml e imagens dos diagramas, inclusive os do banco e o mapa de navegacao
prototipos/  prototipo navegavel das 18 telas do mvp, em html
ferramentas/ scripts que geram a versao imprimivel dos documentos e as telas do prototipo
src/         codigo fonte (comeca na implementacao)
```

as pastas vao sendo criadas conforme cada entrega.

### documentos

| documento | entrega | conteudo |
|---|---|---|
| [documento-visao-requisitos.md](docs/documento-visao-requisitos.md) | 1ª | contexto, escopo, 19 RF, 11 RNF e 12 regras de negocio |
| [casos-de-uso.md](docs/casos-de-uso.md) | 2ª | atores, diagramas de caso de uso, especificacao dos 24 casos de uso, diagramas de atividade de UC13 e UC16, 23 historias de usuario, priorizacao moscow e matriz de rastreabilidade |
| [modelo-de-dados.md](docs/modelo-de-dados.md) | 2ª | diagrama de classes do dominio, modelo conceitual, modelo logico e dicionario de dados das 14 tabelas |
| [mvp-e-prototipos.md](docs/mvp-e-prototipos.md) | 3ª | revisao das entregas anteriores, definicao do mvp, fluxo completo, levantamento das telas, mapa de navegacao, prototipo e rastreabilidade |
| [backlog.md](docs/backlog.md) | 3ª | quadro com as 57 tarefas do projeto, com requisito, prioridade, responsavel e situacao |
| [apresentacao.md](docs/apresentacao.md) | 3ª | roteiro da apresentacao, divisao das falas, perguntas provaveis e checklist final |
| [tecnologias-e-arquitetura.md](docs/tecnologias-e-arquitetura.md) | 2ª | stack definida com justificativa, arquitetura em camadas e como cada RNF sera atendido |

### diagramas

os diagramas sao escritos em plantuml e o arquivo `.puml` fica versionado junto com o `.png` e o `.svg` gerados, pra que qualquer alteracao apareca no diff.

| diagrama | arquivo |
|---|---|
| casos de uso - visao geral | [diagramas/caso-de-uso-geral.png](diagramas/caso-de-uso-geral.png) |
| casos de uso - acesso e cadastros | [diagramas/caso-de-uso-acesso-cadastros.png](diagramas/caso-de-uso-acesso-cadastros.png) |
| casos de uso - documentacao e contratos | [diagramas/caso-de-uso-documentacao.png](diagramas/caso-de-uso-documentacao.png) |
| casos de uso - ordens de servico | [diagramas/caso-de-uso-ordens.png](diagramas/caso-de-uso-ordens.png) |
| casos de uso - consultas e relatorios | [diagramas/caso-de-uso-consultas.png](diagramas/caso-de-uso-consultas.png) |
| atividade - UC13 atribuir ordem | [diagramas/atividade-uc13-atribuir-ordem.png](diagramas/atividade-uc13-atribuir-ordem.png) |
| atividade - UC16 concluir ordem | [diagramas/atividade-uc16-concluir-ordem.png](diagramas/atividade-uc16-concluir-ordem.png) |
| classes - dominio do sgp | [diagramas/diagrama-de-classes.png](diagramas/diagrama-de-classes.png) |
| banco - modelo conceitual | [diagramas/modelo-conceitual.png](diagramas/modelo-conceitual.png) |
| banco - modelo logico | [diagramas/modelo-logico.png](diagramas/modelo-logico.png) |
| arquitetura prevista | [diagramas/arquitetura.png](diagramas/arquitetura.png) |
| mapa de navegacao | [diagramas/mapa-de-navegacao.png](diagramas/mapa-de-navegacao.png) |

pra gerar as imagens de novo depois de mexer em um `.puml`:

```
java -jar plantuml.jar -tpng diagramas/*.puml
java -jar plantuml.jar -tsvg diagramas/*.puml
```

### prototipo

as 18 telas do mvp estao em [prototipos/index.html](prototipos/index.html). é html estatico, sem framework e sem
dependencia de internet: basta abrir o arquivo com dois cliques e navegar clicando, como no sistema de verdade.
as telas mostram tambem os estados que nao aparecem no caminho feliz, como erro de validacao, arquivo recusado,
lista vazia e o motivo de cada prestador inapto.

depois de mexer nas telas, é so rodar:

```
python ferramentas/gerar-prototipo.py
```

### versao imprimivel dos documentos

cada documento em markdown tem um `.html` equivalente, com capa, formatacao a4 e as imagens ja embutidas, pronto pra imprimir ou salvar em pdf. depois de mexer em algum `.md`, é so rodar:

```
pip install markdown
python ferramentas/gerar-html.py
```

## entregas

| entrega | data | conteudo | status |
|---|---|---|---|
| 1 | 14/08/2026 | documento de visao e requisitos | pronto |
| 2 | 08/09/2026 | casos de uso, diagramas de atividade, diagrama de classes e modelagem do banco | pronto |
| 3 | 25/09/2026 | repositorio, backlog, mapa de navegacao, prototipos, mvp e apresentacao | pronto |

## mvp

a primeira versao funcional entrega o fluxo completo do sistema, do pedido do cliente ate a avaliacao do atendimento:
autenticacao, cadastros de apoio, documentacao com controle de validade, situacao cadastral, abertura da ordem,
atribuicao apenas a quem esta apto, execucao, conclusao e avaliacao. sao 16 dos 24 casos de uso e 18 telas.

ficam para depois do mvp os contratos, o aceite da atribuicao pelo prestador, o historico consolidado, os relatorios
e o log de acões criticas. o criterio de corte e a justificativa de cada item estao em
[docs/mvp-e-prototipos.md](docs/mvp-e-prototipos.md).

## como rodar

ainda não tem codigo. as instrucões de instalacao entram aqui quando a implementacao comecar, pela release 1 do
[quadro de tarefas](docs/backlog.md).

# sgp - sistema de gestao de prestadores
## roteiro da apresentacao - 3ª entrega

**versao 1.1 - 25/09/2026**
unicesumar - analise e desenvolvimento de sistemas
imersao profissional - projeto de software - equipe 8

---

## 1. o essencial

a apresentacao é da equipe, mas **a nota é individual**. os dois integrantes falam, e cada um precisa conseguir explicar a propria parte, responder pergunta sobre ela e relaciona-la com o resto do projeto. presenca sem fala nao garante nota.

| item | definicao |
|---|---|
| data | 25/09/2026 |
| equipe | 8 |
| quem fala | luis gustavo boratto de oliveira e igor schiniegoski pallisser, os dois |
| duracao estimada | 15 minutos, com 3 a 5 minutos de perguntas |
| o que sera mostrado | os documentos, os diagramas, o repositorio no github, o quadro de tarefas e o prototipo navegavel |
| o que sera demonstrado ao vivo | o fluxo completo no prototipo, do pedido do cliente ate a avaliacao |

---

## 2. antes de comecar

o trabalho esta publicado em **https://sgp-equipe8.vercel.app**, com o prototipo, os documentos e os diagramas na mesma pagina. é por ali que a apresentacao comeca.

- abrir o site em uma aba e o repositorio do github em outra, na pagina inicial, com o readme visivel;
- deixar o prototipo aberto na tela do mapa, pronto para a demonstracao;
- abrir o `modelo-de-dados.html` e o `mvp-e-prototipos.html` em abas separadas, que sao as versões com capa e imagens embutidas;
- levar a pasta do projeto no pendrive ou no proprio notebook, porque se a internet da sala falhar o prototipo abre offline com dois cliques, sem depender do site nem do github. essa é a razao de ele nao usar framework;
- combinar quem opera o computador enquanto o outro fala.

---

## 3. roteiro

| # | tempo | assunto | quem fala | o que dizer |
|---|---|---|---|---|
| 1 | 1 min | o projeto e o problema | igor | empresa de pequeno e medio porte que contrata terceirizado: cadastro em planilha, documento no drive, contrato na gaveta e servico distribuido no whatsapp. o resultado é documento que vence sem ninguem ver, servico esquecido ou cobrado duas vezes, e escolha de prestador por impressao pessoal |
| 2 | 1 min | publico-alvo e solucao | igor | tres perfis: administrador, prestador e cliente. o sistema centraliza cadastro, documentacao e execucao, com controle de validade e historico de avaliacao |
| 3 | 1,5 min | requisitos e regras | igor | 19 requisitos funcionais, 11 nao funcionais e 12 regras de negocio. destacar RN02, que bloqueia prestador com documento vencido, e RN05, a sequencia dos status |
| 4 | 1 min | evolucao desde a 1ª entrega | igor | o que foi revisado e o que foi acrescentado: diagramas de atividade, classes, modelo de dados e prototipo. mostrar o historico de alteracões dos documentos |
| 5 | 2 min | modelagem | luis | casos de uso por modulo, o diagrama de atividade do UC13 e o diagrama de classes. explicar que as regras de negocio viraram metodo na classe que tem a informacao, como `estaApto()` no prestador |
| 6 | 2 min | banco de dados | luis | modelo conceitual, modelo logico com as 14 tabelas e o dicionario de dados. destacar `prestador_categoria`, que resolve o n:n e sustenta a RN04, e o log sem chave estrangeira |
| 7 | 1,5 min | tecnologias e arquitetura | luis | next.js com postgresql e prisma na vercel, monolito em camadas. a frase que resume: nenhuma permissao é decidida na tela, a rota de api confere o perfil antes de qualquer operacao |
| 8 | 1 min | repositorio e organizacao do trabalho | luis | mostrar o github, com as pastas docs, diagramas, prototipos e ferramentas, os commits identificando quem fez o que, e o quadro de 57 tarefas com responsavel e situacao. mencionar que o mesmo conteudo esta publicado em sgp-equipe8.vercel.app, entao qualquer pessoa abre sem baixar nada |
| 9 | 1,5 min | mvp | luis | o criterio: entra o que for necessario para o fluxo funcionar do inicio ao fim. 16 casos de uso de 24, 60 pontos de 85. o que ficou de fora e por que, com contrato e relatorio como exemplos |
| 10 | 2 min | navegacao e prototipo | igor | mapa de navegacao, as 18 telas por perfil e a diferenca de tamanho entre os perfis, que é recorte de permissao e nao falta de tela |
| 11 | 2 min | demonstracao do fluxo completo | igor opera, luis narra a regra | percorrer no prototipo: cliente abre a solicitacao (T17), administrador atribui vendo so os aptos e o motivo de cada inapto (T12), prestador executa e conclui com relato (T14), cliente avalia (T18) |
| 12 | 1 min | proximos passos | luis | releases 1 a 3 como o caminho ate o mvp, e a release 4 com contratos, log e relatorio. a implementacao comeca pelas telas ja prototipadas |

---

## 4. o que cada um precisa saber explicar

os criterios de avaliacao individual do manual sao dominio do conteudo, clareza, compreensao do projeto como um todo, autoria, capacidade de responder e participacao.

### igor schiniegoski pallisser

- por que cada requisito existe e de qual dor ele nasceu;
- como um requisito virou caso de uso, historia e depois tela;
- por que o cliente nao enxerga a lista de prestadores;
- como o prototipo representa validacao, erro, estado vazio e feedback;
- o caminho de qualquer tela ate a inicial, no mapa de navegacao.

### luis gustavo boratto de oliveira

- por que o endereco virou coluna e o tipo de documento virou tabela;
- onde cada regra de negocio é verificada, e por que a verificacao de aptidao é uma funcao unica;
- por que a atribuicao revalida a aptidao no servidor mesmo tendo filtrado a lista antes;
- por que nenhuma tabela apaga registro;
- o criterio do mvp e o motivo de contrato e relatorio ficarem de fora.

### os dois

- o problema, o objetivo e os tres perfis;
- o fluxo completo do sistema, ponta a ponta;
- o que cada um fez e como isso se conecta com a parte do outro.

---

## 5. perguntas provaveis

| pergunta | resposta curta |
|---|---|
| por que nao usar um erp pronto? | os que resolvem isso ou custam caro demais para o porte do cliente, ou tratam terceirizado como modulo pequeno e complicado de configurar. o recorte focado entrega valor rapido e cabe no prazo |
| o que acontece se o documento vencer no meio de um servico? | o prestador passa a pendente e nao recebe nova ordem, mas continua podendo concluir o que ja estava em execucao. é a mesma logica da RN03 para contrato |
| por que a ordem concluida nao pode ser editada? | porque ela vira historico e alimenta a avaliacao e o relatorio. correcao se faz por cancelamento com justificativa e abertura de nova ordem, o que deixa rastro |
| como o sistema impede que um prestador veja a ordem de outro? | o recorte é aplicado na rota de api pelo usuario da sessao. esconder o botao na tela é so conforto visual, quem recusa a requisicao é o servidor |
| por que escolheram essa stack? | familiaridade da equipe, plano gratuito e um projeto so entregando tela e api, o que reduz configuracao e deixa um deploy unico |
| quanto do sistema ja esta pronto? | a documentacao, a modelagem completa e o prototipo navegavel das 18 telas do mvp. a implementacao comeca pela release 1, ja planejada no quadro de tarefas |
| por que 18 telas e nao mais? | sao as telas que o mvp exige. as funcionalidades que ficaram fora do mvp nao ganharam tela, justamente para nao prometer o que nao sera construido |
| o prototipo é o sistema funcionando? | nao. é navegavel e mostra os estados reais de cada tela, mas nao grava dado. o codigo comeca na release 1 |

---

## 6. checklist final do manual

| item exigido | situacao |
|---|---|
| todos os integrantes identificados no documento e no repositorio | pronto, no readme e em cada documento |
| documentacao com as correcões das entregas anteriores | pronto, secao 2 do documento de mvp e prototipos |
| historico de alteracões atualizado | pronto, no rodape de cada documento |
| nomenclatura coerente entre requisito, regra, diagrama, banco e tela | pronto, conferido na revisao |
| diagramas e prototipos legiveis | pronto, com png e svg versionados |
| github existente atualizado, sem repositorio novo | pronto, é o mesmo repositorio desde a 1ª entrega |
| readme explicando o projeto | pronto |
| arquivos organizados e acessiveis | pronto: docs, diagramas, prototipos e ferramentas |
| commits permitindo identificar a evolucao e a contribuicao | pronto |
| backlog com tarefas, prioridades, responsaveis e estados | pronto, em backlog.md |
| tecnologias definidas e justificadas | pronto, em tecnologias-e-arquitetura.md |
| diagrama simples de arquitetura | pronto, em diagramas/arquitetura.png |
| mapa de navegacao | pronto, em diagramas/mapa-de-navegacao.png |
| esboco de todas as telas do mvp | pronto, as 18 telas estao no prototipo |
| prototipo compreensivel das telas principais | pronto, prototipo navegavel em html |
| mvp separado do desejavel e do futuro | pronto, secao 3 do documento de mvp e prototipos |
| pelo menos um fluxo completo definido | pronto, secao 4 do mesmo documento |
| links e permissões de acesso testados | as 32 paginas publicadas responderam, e nenhum link interno dos documentos esta quebrado. falta so abrir o repositorio em uma janela anonima no dia, para confirmar que ele esta publico |
| todos sabem a propria parte na apresentacao | secao 3 deste documento |
| todos conseguem explicar as proprias contribuicões | secao 4 deste documento |
| todos revisaram o projeto completo | fazer a ultima leitura na vespera, dia 24 |

---

## historico de alteracões

| versao | data | alteracao |
|---|---|---|
| 1.0 | 22/09/2026 | primeira versao do roteiro, com a divisao das falas, as perguntas provaveis e o checklist do manual |
| 1.1 | 22/09/2026 | o trabalho passou a ter endereco publicado, entao a abertura da apresentacao comeca por ele, com a copia local como plano B |

# sgp - sistema de gestao de prestadores
## documento de visao e requisitos

**versao 1.0 - 14/08/2026 - 1ª entrega**
unicesumar - analise e desenvolvimento de sistemas
imersao profissional - projeto de software - equipe 8

---

## 1. identificacao do projeto

| item | descricao |
|---|---|
| nome provisorio do sistema | sgp - sistema de gestao de prestadores |
| tema da equipe | plataforma para controle de prestadores de servicos |
| equipe | equipe 8 |
| integrantes | luis gustavo boratto de oliveira, igor schiniegoski pallisser, lucas mendes |
| versao do documento | 1.0 - primeira entrega |

o sgp é um sistema web para empresas que trabalham com prestadores de servico terceirizados. ele reune em um lugar só o cadastro dos prestadores, dos clientes e das categorias de servico, guarda os documentos e contratos de cada prestador com a data de validade, e controla as ordens de servico desde a abertura ate a conclusao, passando pela atribuicao a um prestador. no fim de cada atendimento o cliente avalia o servico, e essas notas alimentam o historico e os relatórios de desempenho que ajudam o gestor a decidir quem chamar da próxima vez.

---

## 2. contexto e problema

### 2.1 situacao que motivou a criacao do sistema

muita empresa de pequeno e médio porte não executa todos os servicos com equipe própria. ela mantém uma rede de prestadores terceirizados (autônomos, mei e pequenas empresas) que são acionados conforme a demanda: manutencao predial, instalacao, limpeza, assistência técnica, treinamentos e por aí vai. o problema é que esse controle quase sempre é feito fora de qualquer sistema.

o que se vê na prática é o cadastro dos prestadores em uma planilha do excel, os documentos (rg, cpf, cnpj, certidões, comprovante de curso, apólice de seguro) espalhados em pastas do drive ou no email, os contratos impressos em um armário, e a distribuicao dos servicos acontecendo por grupo de whatsapp. cada uma dessas partes funciona sozinha, mas nenhuma conversa com a outra.

### 2.2 quem enfrenta o problema

quem sente primeiro é o responsável por contratar e acompanhar os terceirizados, que pode ser o gestor operacional, o setor administrativo ou o dono da empresa. ele é cobrado quando um servico atrasa, quando o cliente reclama e quando aparece uma fiscalizacao pedindo a documentacao de quem esteve na obra. o prestador também é prejudicado, porque não tem clareza do que foi atribuido a ele, dos prazos e do que já entregou. e o cliente final fica sem nenhuma previsibilidade de quando o servico vai ser feito e por quem.

### 2.3 como o processo ocorre atualmente

- o prestador é cadastrado em uma planilha, com os campos que quem digitou achou importante na hora;
- os documentos são pedidos por whatsapp ou email e ficam guardados sem controle de validade, então ninguém percebe quando vencem;
- quando surge uma demanda, o gestor lembra "de cabeça" de quem costuma atender aquele tipo de servico e chama no whatsapp;
- o acompanhamento é feito por mensagem solta, sem status formal, e a conclusao é registrada, quando é, em outra planilha;
- a avaliacao do atendimento não existe de forma estruturada, ela fica no "fulano é bom" ou "com esse não dá certo";
- quando alguém pede um histórico ou um número consolidado, é preciso garimpar planilha, conversa e email pra montar a resposta.

### 2.4 justificativa

esse jeito de trabalhar gera problema real e mensurável. contratar um prestador com documento vencido expõe a empresa a risco jurídico e a multa, e em alguns setores impede que o profissional entre no local do servico. a falta de um registro único faz o mesmo servico ser cobrado duas vezes ou simplesmente ser esquecido. sem histórico de avaliacao, a escolha de quem contratar continua sendo por impressão pessoal, e o conhecimento vai embora junto com o funcionário que saiu da empresa.

vale desenvolver o sistema porque o processo é repetitivo, tem regra clara e volume suficiente pra justificar a automatizacao. as ferramentas de mercado que resolvem isso ou são caras demais pro porte do cliente ou são erps completos, em que o controle de terceirizados é um módulo pequeno e complicado de configurar. um sistema focado só nesse recorte entrega valor rápido e é viável de construir no prazo da disciplina.

---

## 3. objetivos

### 3.1 objetivo geral

desenvolver uma plataforma web para controlar o cadastro, a documentacao e a execucao dos servicos prestados por profissionais terceirizados, centralizando em um único sistema as informacões que hoje ficam espalhadas em planilhas, mensagens e arquivos.

### 3.2 objetivos especificos

- centralizar o cadastro de prestadores, clientes e categorias de servico em uma base única e padronizada;
- controlar a validade dos documentos e dos contratos de cada prestador, avisando o gestor antes do vencimento;
- registrar, atribuir e acompanhar as ordens de servico do início ao fim, com status e responsável definidos em cada etapa;
- manter o histórico completo dos atendimentos e das avaliacões recebidas por cada prestador;
- gerar relatórios de desempenho que apoiem a decisao de qual prestador acionar em uma nova demanda;
- garantir que cada perfil de usuário só enxergue e altere o que é da sua responsabilidade.

---

## 4. publico-alvo e perfis de usuario

o público-alvo são empresas de pequeno e médio porte que contratam servico terceirizado com frequência, e os próprios prestadores que atendem essas empresas. o sistema prevê três perfis.

| perfil | necessidades | responsabilidades | permissões |
|---|---|---|---|
| **administrador** (gestor da empresa contratante) | enxergar toda a rede de prestadores, saber quem está apto a atender, distribuir as demandas e acompanhar o resultado | cadastrar prestadores e clientes, conferir documentos, manter contratos, abrir e atribuir ordens de servico | acesso total: cria, edita, consulta e inativa qualquer registro, altera situacao cadastral, cancela ordem e emite todos os relatórios |
| **prestador de servico** | saber o que foi atribuido a ele, o prazo e o que já entregou, e manter a documentacao em dia sem depender de cobranca | enviar e renovar seus documentos, aceitar ou recusar a atribuicao, atualizar o andamento e concluir o servico | acesso restrito: vê e edita apenas o próprio cadastro, os próprios documentos e as ordens atribuidas a ele. não vê dado de outro prestador nem valor de contrato de terceiros |
| **cliente** | solicitar um servico, saber em que pé está e registrar se foi bem atendido | abrir a solicitacao com a descricao do que precisa e avaliar o atendimento depois de concluído | acesso restrito: abre solicitacao, consulta as próprias ordens e o próprio histórico, e lanca a avaliacao. não vê a lista de prestadores nem os dados internos da empresa |

---

## 5. escopo

### 5.1 o que faz parte da primeira versao

- autenticacao por login e senha, com controle de acesso por perfil;
- cadastro de prestadores, clientes e categorias de servico;
- catálogo de servicos vinculado às categorias;
- upload de documentos do prestador com tipo e data de validade, e painel de vencimentos;
- cadastro de contratos com vigência, valor e arquivo anexo;
- controle da situacao cadastral do prestador (ativo, pendente, bloqueado, inativo);
- abertura, atribuicao e acompanhamento das ordens de servico por status;
- avaliacao do atendimento pelo cliente ao final da ordem;
- histórico de atendimentos por prestador e por cliente;
- relatórios de desempenho e de servicos realizados por período;
- registro de log das acões críticas do sistema.

### 5.2 o que nao faz parte do projeto neste momento

- pagamento online ao prestador e integracao com meio de pagamento ou banco;
- emissao de nota fiscal e integracao com sistema fiscal ou contábil;
- assinatura digital de contrato com certificado icp-brasil (o contrato é anexado já assinado);
- aplicativo nativo pra android e ios, o acesso é pelo navegador do celular;
- chat interno e envio automático de mensagem por whatsapp;
- geolocalizacao e rastreio do prestador em tempo real;
- controle de estoque, de material e de folha de pagamento;
- integracao com erp ou com sistema legado do cliente.

### 5.3 restricões

| tipo | restricao |
|---|---|
| prazo | o desenvolvimento acontece dentro do calendário da disciplina, com as entregas em 14/08, 08/09 e 25/09 de 2026. o escopo do mvp foi reduzido pra caber nesse período |
| equipe | três integrantes, conciliando o projeto com as demais disciplinas do curso |
| tecnologia | serão usadas tecnologias que a equipe já domina ou consegue aprender no prazo, priorizando ferramenta gratuita ou com plano free |
| hospedagem | o sistema será publicado em servico de nuvem com plano gratuito, o que limita processamento, espaco de armazenamento e volume de dados de teste |
| acesso | o uso exige internet, o sistema não funciona offline |
| dados | não haverá integracao com base externa, os dados de teste serão fictícios pra não expor dado pessoal real (lgpd) |

---

## 6. requisitos funcionais

| código | requisito | descricao |
|---|---|---|
| RF01 | autenticar usuário | o sistema deve permitir o acesso por email e senha, identificando o perfil do usuário e liberando apenas as funcões correspondentes |
| RF02 | manter cadastro de prestadores | o sistema deve permitir cadastrar, consultar, editar e inativar prestadores, com nome ou razao social, cpf ou cnpj, telefone, email e endereco |
| RF03 | manter cadastro de clientes | o sistema deve permitir cadastrar, consultar, editar e inativar clientes, com os dados de identificacao e contato |
| RF04 | manter categorias de servico | o sistema deve permitir cadastrar e editar categorias de servico (ex: elétrica, hidráulica, limpeza) usadas pra classificar servicos e prestadores |
| RF05 | manter catalogo de servicos | o sistema deve permitir cadastrar servicos com nome, descricao, categoria, valor de referência e prazo padrao de execucao |
| RF06 | habilitar prestador em categorias | o sistema deve permitir vincular um prestador a uma ou mais categorias, indicando em que tipo de servico ele está habilitado a atuar |
| RF07 | enviar documentos do prestador | o sistema deve permitir anexar documentos ao cadastro do prestador, informando o tipo, a data de emissao e a data de validade |
| RF08 | alertar documentos vencidos | o sistema deve exibir ao administrador um painel com os documentos vencidos e os que vencem nos próximos 30 dias |
| RF09 | controlar situacao cadastral | o sistema deve permitir alterar a situacao do prestador entre ativo, pendente, bloqueado e inativo, registrando o motivo, a data e o usuário responsável |
| RF10 | manter contratos | o sistema deve permitir cadastrar contratos vinculados ao prestador, com data de início, data de término, valor e arquivo anexo |
| RF11 | registrar ordem de servico | o sistema deve permitir abrir uma ordem de servico informando cliente, servico, descricao do problema, prazo desejado e prioridade |
| RF12 | atribuir ordem a um prestador | o sistema deve permitir que o administrador atribua uma ordem de servico a um prestador apto, exibindo apenas os prestadores habilitados na categoria do servico |
| RF13 | acompanhar a ordem de servico | o sistema deve controlar o status da ordem (aberta, atribuida, em execucao, concluída, cancelada) e registrar a data, o usuário e a observacao de cada mudanca |
| RF14 | consultar ordens do prestador | o sistema deve exibir ao prestador logado apenas as ordens atribuidas a ele, permitindo atualizar o andamento e concluir o servico |
| RF15 | avaliar o atendimento | o sistema deve permitir que o cliente registre uma nota de 1 a 5 e um comentário depois que a ordem for concluída |
| RF16 | consultar historico de atendimentos | o sistema deve exibir o histórico de ordens por prestador e por cliente, com filtro por período, status e categoria |
| RF17 | gerar relatorio de desempenho | o sistema deve gerar um relatório por prestador com a quantidade de servicos concluídos, a nota média recebida e o percentual de servicos entregues dentro do prazo |
| RF18 | gerar relatorio de servicos por periodo | o sistema deve gerar um relatório de ordens abertas, concluídas e canceladas em um intervalo de datas, agrupadas por categoria |
| RF19 | registrar log de acões criticas | o sistema deve registrar em log a mudanca de situacao cadastral, a atribuicao e o cancelamento de ordem, guardando usuário, data e hora |

---

## 7. requisitos nao funcionais

| código | categoria | requisito |
|---|---|---|
| RNF01 | seguranca | as senhas devem ser armazenadas com hash (bcrypt ou equivalente), nunca em texto puro no banco |
| RNF02 | seguranca | toda regra de permissao deve ser validada no servidor, e não apenas escondendo o botao na tela. uma requisicao feita por um perfil sem direito deve ser recusada |
| RNF03 | seguranca | o sistema deve encerrar a sessao automaticamente após 30 minutos sem atividade |
| RNF04 | usabilidade | a interface deve ser responsiva e utilizável em tela de notebook (1366x768) e em celular, sem rolagem horizontal |
| RNF05 | usabilidade | toda acao que altera ou apaga dado deve exibir confirmacao e mensagem de retorno informando se deu certo ou qual foi o erro |
| RNF06 | desempenho | as listagens devem usar paginacao e responder em até 3 segundos com uma base de 5 mil registros |
| RNF07 | compatibilidade | o sistema deve funcionar nas versões atuais do google chrome, microsoft edge e mozilla firefox |
| RNF08 | disponibilidade | o sistema deve ser hospedado em nuvem, com backup diário do banco de dados e possibilidade de restauracao |
| RNF09 | armazenamento | o upload de documentos deve aceitar os formatos pdf, jpg e png, com limite de 10 mb por arquivo |
| RNF10 | privacidade | os dados pessoais devem ficar visíveis apenas aos perfis autorizados, atendendo a lgpd, e a conta deve poder ser excluída ou anonimizada mediante solicitacao |
| RNF11 | manutenibilidade | o código deve ser versionado no github, com padrao de nomes definido, readme e commits identificáveis por integrante |

---

## 8. regras de negocio

| código | regra | descricao |
|---|---|---|
| RN01 | prestador precisa estar ativo | uma ordem de servico só pode ser atribuida a um prestador cuja situacao cadastral esteja como "ativo" |
| RN02 | documento vencido bloqueia o prestador | quando um documento obrigatório do prestador vence, a situacao dele passa automaticamente pra "pendente" e ele deixa de aparecer na lista de atribuicao até regularizar |
| RN03 | contrato vigente obrigatorio | prestador sem contrato dentro da vigência não pode receber nova atribuicao, mas continua podendo concluir as ordens que já estavam em execucao |
| RN04 | atribuicao respeita a categoria | o prestador só pode ser atribuido a uma ordem cujo servico pertenca a uma categoria em que ele está habilitado |
| RN05 | sequencia dos status | a ordem segue a sequência aberta → atribuida → em execucao → concluída. não é permitido pular etapa nem voltar pra um status anterior |
| RN06 | ordem concluida é imutavel | depois de concluída, a ordem não pode mais ser editada. a correcao de um erro só pode ser feita pelo administrador, por meio de cancelamento com justificativa e abertura de uma nova ordem |
| RN07 | cancelamento exige motivo | o cancelamento de uma ordem só pode acontecer antes da conclusao, exige um motivo com no mínimo 10 caracteres e fica registrado no log |
| RN08 | avaliacao unica e pelo cliente | a avaliacao só pode ser lancada pelo cliente vinculado à ordem, somente depois que ela for concluída, e apenas uma vez por ordem |
| RN09 | calculo da nota media | a nota média do prestador é a média aritmética das avaliacões dos últimos 12 meses. prestador com menos de três avaliacões no período aparece como "sem histórico suficiente" |
| RN10 | cpf e cnpj unicos | não pode existir mais de um cadastro ativo com o mesmo cpf ou cnpj, e o número precisa ser válido pelo dígito verificador |
| RN11 | prestador com ordem aberta nao é inativado | não é permitido inativar um prestador que tenha ordem atribuida ou em execucao. antes é preciso concluir ou realocar essas ordens |
| RN12 | prazo e atraso | a ordem é considerada em atraso quando a data atual passa do prazo combinado e o status ainda não é "concluída". esse indicador entra no relatório de desempenho |

---

## 9. glossario

| termo | significado |
|---|---|
| prestador | profissional autônomo, mei ou empresa contratada pra executar um servico, sem vínculo empregatício com a contratante |
| ordem de servico (os) | registro de uma demanda de servico, do pedido do cliente até a conclusao pelo prestador |
| situacao cadastral | estado do prestador dentro do sistema: ativo, pendente, bloqueado ou inativo |
| categoria de servico | agrupamento que classifica os servicos e define em que área o prestador está habilitado |
| mvp | produto mínimo viável, a menor versao do sistema que já entrega valor e permite usar o fluxo completo |

---

## 10. referencias

- orientacões para as entregas - projeto de software, 1º bimestre. documento da disciplina, unicesumar, 2026.
- sommerville, i. *engenharia de software*. 10. ed. sao paulo: pearson, 2018.
- brasil. lei nº 13.709, de 14 de agosto de 2018. lei geral de protecao de dados pessoais (lgpd).
- levantamento informal feito pela equipe com base na rotina observada em empresas que contratam servico terceirizado.

---

## historico de alteracões

| versao | data | alteracao |
|---|---|---|
| 1.0 | 14/08/2026 | primeira versao do documento, entregue na 1ª entrega |

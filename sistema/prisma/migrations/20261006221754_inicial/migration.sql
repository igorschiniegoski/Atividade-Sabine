-- CreateTable
CREATE TABLE "usuario" (
    "id_usuario" SERIAL NOT NULL,
    "nome" VARCHAR(120) NOT NULL,
    "email" VARCHAR(150) NOT NULL,
    "senha_hash" VARCHAR(60) NOT NULL,
    "perfil" VARCHAR(15) NOT NULL,
    "ativo" BOOLEAN NOT NULL DEFAULT true,
    "tentativas_falhas" SMALLINT NOT NULL DEFAULT 0,
    "bloqueado_ate" TIMESTAMP(3),
    "ultimo_acesso_em" TIMESTAMP(3),
    "criado_em" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "usuario_pkey" PRIMARY KEY ("id_usuario")
);

-- CreateTable
CREATE TABLE "prestador" (
    "id_prestador" SERIAL NOT NULL,
    "id_usuario" INTEGER,
    "tipo_pessoa" CHAR(1) NOT NULL,
    "nome_razao_social" VARCHAR(150) NOT NULL,
    "nome_fantasia" VARCHAR(120),
    "cpf_cnpj" VARCHAR(14) NOT NULL,
    "telefone" VARCHAR(20) NOT NULL,
    "email" VARCHAR(150),
    "logradouro" VARCHAR(150) NOT NULL,
    "numero" VARCHAR(10) NOT NULL,
    "complemento" VARCHAR(60),
    "bairro" VARCHAR(60) NOT NULL,
    "cidade" VARCHAR(60) NOT NULL,
    "uf" CHAR(2) NOT NULL,
    "cep" CHAR(8) NOT NULL,
    "situacao" VARCHAR(12) NOT NULL DEFAULT 'pendente',
    "criado_em" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "atualizado_em" TIMESTAMP(3),

    CONSTRAINT "prestador_pkey" PRIMARY KEY ("id_prestador")
);

-- CreateTable
CREATE TABLE "cliente" (
    "id_cliente" SERIAL NOT NULL,
    "id_usuario" INTEGER,
    "tipo_pessoa" CHAR(1) NOT NULL,
    "nome_razao_social" VARCHAR(150) NOT NULL,
    "nome_fantasia" VARCHAR(120),
    "cpf_cnpj" VARCHAR(14) NOT NULL,
    "telefone" VARCHAR(20) NOT NULL,
    "email" VARCHAR(150),
    "logradouro" VARCHAR(150) NOT NULL,
    "numero" VARCHAR(10) NOT NULL,
    "complemento" VARCHAR(60),
    "bairro" VARCHAR(60) NOT NULL,
    "cidade" VARCHAR(60) NOT NULL,
    "uf" CHAR(2) NOT NULL,
    "cep" CHAR(8) NOT NULL,
    "ativo" BOOLEAN NOT NULL DEFAULT true,
    "criado_em" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "cliente_pkey" PRIMARY KEY ("id_cliente")
);

-- CreateTable
CREATE TABLE "categoria_servico" (
    "id_categoria" SERIAL NOT NULL,
    "nome" VARCHAR(60) NOT NULL,
    "descricao" VARCHAR(255),
    "ativa" BOOLEAN NOT NULL DEFAULT true,

    CONSTRAINT "categoria_servico_pkey" PRIMARY KEY ("id_categoria")
);

-- CreateTable
CREATE TABLE "servico" (
    "id_servico" SERIAL NOT NULL,
    "id_categoria" INTEGER NOT NULL,
    "nome" VARCHAR(120) NOT NULL,
    "descricao" TEXT,
    "valor_referencia" DECIMAL(10,2),
    "prazo_padrao_dias" SMALLINT NOT NULL,
    "ativo" BOOLEAN NOT NULL DEFAULT true,

    CONSTRAINT "servico_pkey" PRIMARY KEY ("id_servico")
);

-- CreateTable
CREATE TABLE "prestador_categoria" (
    "id_prestador" INTEGER NOT NULL,
    "id_categoria" INTEGER NOT NULL,
    "habilitado_em" DATE NOT NULL,
    "ativa" BOOLEAN NOT NULL DEFAULT true,

    CONSTRAINT "prestador_categoria_pkey" PRIMARY KEY ("id_prestador","id_categoria")
);

-- CreateTable
CREATE TABLE "tipo_documento" (
    "id_tipo_documento" SERIAL NOT NULL,
    "nome" VARCHAR(60) NOT NULL,
    "obrigatorio" BOOLEAN NOT NULL,
    "exige_validade" BOOLEAN NOT NULL,
    "ativo" BOOLEAN NOT NULL DEFAULT true,

    CONSTRAINT "tipo_documento_pkey" PRIMARY KEY ("id_tipo_documento")
);

-- CreateTable
CREATE TABLE "documento" (
    "id_documento" SERIAL NOT NULL,
    "id_prestador" INTEGER NOT NULL,
    "id_tipo_documento" INTEGER NOT NULL,
    "nome_arquivo" VARCHAR(255) NOT NULL,
    "arquivo_url" VARCHAR(500) NOT NULL,
    "tamanho_bytes" INTEGER NOT NULL,
    "data_emissao" DATE NOT NULL,
    "data_validade" DATE,
    "versao_atual" BOOLEAN NOT NULL DEFAULT true,
    "enviado_por" INTEGER NOT NULL,
    "enviado_em" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "documento_pkey" PRIMARY KEY ("id_documento")
);

-- CreateTable
CREATE TABLE "contrato" (
    "id_contrato" SERIAL NOT NULL,
    "id_prestador" INTEGER NOT NULL,
    "numero" VARCHAR(30) NOT NULL,
    "data_inicio" DATE NOT NULL,
    "data_fim" DATE NOT NULL,
    "valor" DECIMAL(12,2),
    "arquivo_url" VARCHAR(500) NOT NULL,
    "criado_em" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "contrato_pkey" PRIMARY KEY ("id_contrato")
);

-- CreateTable
CREATE TABLE "historico_situacao" (
    "id_historico" SERIAL NOT NULL,
    "id_prestador" INTEGER NOT NULL,
    "situacao_anterior" VARCHAR(12),
    "situacao_nova" VARCHAR(12) NOT NULL,
    "motivo" VARCHAR(255) NOT NULL,
    "id_usuario" INTEGER,
    "alterado_em" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "historico_situacao_pkey" PRIMARY KEY ("id_historico")
);

-- CreateTable
CREATE TABLE "ordem_servico" (
    "id_ordem" SERIAL NOT NULL,
    "numero" VARCHAR(20) NOT NULL,
    "id_cliente" INTEGER NOT NULL,
    "id_servico" INTEGER NOT NULL,
    "id_prestador" INTEGER,
    "descricao" TEXT NOT NULL,
    "local_atendimento" VARCHAR(200),
    "prioridade" VARCHAR(10) NOT NULL DEFAULT 'normal',
    "prazo" DATE NOT NULL,
    "status" VARCHAR(12) NOT NULL DEFAULT 'aberta',
    "aberta_por" INTEGER NOT NULL,
    "data_abertura" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "data_atribuicao" TIMESTAMP(3),
    "data_inicio_execucao" TIMESTAMP(3),
    "data_conclusao" TIMESTAMP(3),
    "relato_conclusao" TEXT,
    "motivo_cancelamento" VARCHAR(255),
    "entregue_no_prazo" BOOLEAN,

    CONSTRAINT "ordem_servico_pkey" PRIMARY KEY ("id_ordem")
);

-- CreateTable
CREATE TABLE "andamento_ordem" (
    "id_andamento" SERIAL NOT NULL,
    "id_ordem" INTEGER NOT NULL,
    "status_anterior" VARCHAR(12),
    "status_novo" VARCHAR(12) NOT NULL,
    "observacao" TEXT,
    "id_usuario" INTEGER NOT NULL,
    "registrado_em" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "andamento_ordem_pkey" PRIMARY KEY ("id_andamento")
);

-- CreateTable
CREATE TABLE "avaliacao" (
    "id_avaliacao" SERIAL NOT NULL,
    "id_ordem" INTEGER NOT NULL,
    "nota" SMALLINT NOT NULL,
    "comentario" VARCHAR(500),
    "avaliado_em" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "avaliacao_pkey" PRIMARY KEY ("id_avaliacao")
);

-- CreateTable
CREATE TABLE "log_acao" (
    "id_log" SERIAL NOT NULL,
    "id_usuario" INTEGER NOT NULL,
    "acao" VARCHAR(40) NOT NULL,
    "entidade" VARCHAR(40) NOT NULL,
    "entidade_id" INTEGER NOT NULL,
    "detalhe" TEXT,
    "registrado_em" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "log_acao_pkey" PRIMARY KEY ("id_log")
);

-- CreateIndex
CREATE UNIQUE INDEX "usuario_email_key" ON "usuario"("email");

-- CreateIndex
CREATE UNIQUE INDEX "prestador_id_usuario_key" ON "prestador"("id_usuario");

-- CreateIndex
CREATE UNIQUE INDEX "prestador_cpf_cnpj_key" ON "prestador"("cpf_cnpj");

-- CreateIndex
CREATE INDEX "prestador_situacao_idx" ON "prestador"("situacao");

-- CreateIndex
CREATE UNIQUE INDEX "cliente_id_usuario_key" ON "cliente"("id_usuario");

-- CreateIndex
CREATE UNIQUE INDEX "cliente_cpf_cnpj_key" ON "cliente"("cpf_cnpj");

-- CreateIndex
CREATE UNIQUE INDEX "categoria_servico_nome_key" ON "categoria_servico"("nome");

-- CreateIndex
CREATE UNIQUE INDEX "tipo_documento_nome_key" ON "tipo_documento"("nome");

-- CreateIndex
CREATE INDEX "documento_data_validade_versao_atual_idx" ON "documento"("data_validade", "versao_atual");

-- CreateIndex
CREATE UNIQUE INDEX "ordem_servico_numero_key" ON "ordem_servico"("numero");

-- CreateIndex
CREATE INDEX "ordem_servico_status_prazo_idx" ON "ordem_servico"("status", "prazo");

-- CreateIndex
CREATE INDEX "ordem_servico_id_prestador_idx" ON "ordem_servico"("id_prestador");

-- CreateIndex
CREATE INDEX "ordem_servico_id_cliente_idx" ON "ordem_servico"("id_cliente");

-- CreateIndex
CREATE UNIQUE INDEX "avaliacao_id_ordem_key" ON "avaliacao"("id_ordem");

-- CreateIndex
CREATE INDEX "avaliacao_avaliado_em_idx" ON "avaliacao"("avaliado_em");

-- CreateIndex
CREATE INDEX "log_acao_registrado_em_entidade_idx" ON "log_acao"("registrado_em", "entidade");

-- AddForeignKey
ALTER TABLE "prestador" ADD CONSTRAINT "prestador_id_usuario_fkey" FOREIGN KEY ("id_usuario") REFERENCES "usuario"("id_usuario") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "cliente" ADD CONSTRAINT "cliente_id_usuario_fkey" FOREIGN KEY ("id_usuario") REFERENCES "usuario"("id_usuario") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "servico" ADD CONSTRAINT "servico_id_categoria_fkey" FOREIGN KEY ("id_categoria") REFERENCES "categoria_servico"("id_categoria") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "prestador_categoria" ADD CONSTRAINT "prestador_categoria_id_prestador_fkey" FOREIGN KEY ("id_prestador") REFERENCES "prestador"("id_prestador") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "prestador_categoria" ADD CONSTRAINT "prestador_categoria_id_categoria_fkey" FOREIGN KEY ("id_categoria") REFERENCES "categoria_servico"("id_categoria") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "documento" ADD CONSTRAINT "documento_id_prestador_fkey" FOREIGN KEY ("id_prestador") REFERENCES "prestador"("id_prestador") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "documento" ADD CONSTRAINT "documento_id_tipo_documento_fkey" FOREIGN KEY ("id_tipo_documento") REFERENCES "tipo_documento"("id_tipo_documento") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "documento" ADD CONSTRAINT "documento_enviado_por_fkey" FOREIGN KEY ("enviado_por") REFERENCES "usuario"("id_usuario") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "contrato" ADD CONSTRAINT "contrato_id_prestador_fkey" FOREIGN KEY ("id_prestador") REFERENCES "prestador"("id_prestador") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "historico_situacao" ADD CONSTRAINT "historico_situacao_id_prestador_fkey" FOREIGN KEY ("id_prestador") REFERENCES "prestador"("id_prestador") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "historico_situacao" ADD CONSTRAINT "historico_situacao_id_usuario_fkey" FOREIGN KEY ("id_usuario") REFERENCES "usuario"("id_usuario") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "ordem_servico" ADD CONSTRAINT "ordem_servico_id_cliente_fkey" FOREIGN KEY ("id_cliente") REFERENCES "cliente"("id_cliente") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "ordem_servico" ADD CONSTRAINT "ordem_servico_id_servico_fkey" FOREIGN KEY ("id_servico") REFERENCES "servico"("id_servico") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "ordem_servico" ADD CONSTRAINT "ordem_servico_id_prestador_fkey" FOREIGN KEY ("id_prestador") REFERENCES "prestador"("id_prestador") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "ordem_servico" ADD CONSTRAINT "ordem_servico_aberta_por_fkey" FOREIGN KEY ("aberta_por") REFERENCES "usuario"("id_usuario") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "andamento_ordem" ADD CONSTRAINT "andamento_ordem_id_ordem_fkey" FOREIGN KEY ("id_ordem") REFERENCES "ordem_servico"("id_ordem") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "andamento_ordem" ADD CONSTRAINT "andamento_ordem_id_usuario_fkey" FOREIGN KEY ("id_usuario") REFERENCES "usuario"("id_usuario") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "avaliacao" ADD CONSTRAINT "avaliacao_id_ordem_fkey" FOREIGN KEY ("id_ordem") REFERENCES "ordem_servico"("id_ordem") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "log_acao" ADD CONSTRAINT "log_acao_id_usuario_fkey" FOREIGN KEY ("id_usuario") REFERENCES "usuario"("id_usuario") ON DELETE RESTRICT ON UPDATE CASCADE;

-- restricoes check do dicionario de dados (secao 6). o prisma nao gera check sozinho,
-- entao elas foram escritas a mao aqui. valem como segunda barreira alem da validacao da aplicacao (RNF02).

ALTER TABLE "usuario" ADD CONSTRAINT "usuario_perfil_check"
  CHECK ("perfil" IN ('administrador', 'prestador', 'cliente'));

ALTER TABLE "prestador" ADD CONSTRAINT "prestador_tipo_pessoa_check" CHECK ("tipo_pessoa" IN ('F', 'J'));
ALTER TABLE "prestador" ADD CONSTRAINT "prestador_situacao_check"
  CHECK ("situacao" IN ('ativo', 'pendente', 'bloqueado', 'inativo'));
ALTER TABLE "prestador" ADD CONSTRAINT "prestador_uf_check" CHECK ("uf" IN (
  'AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA',
  'PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'));

ALTER TABLE "cliente" ADD CONSTRAINT "cliente_tipo_pessoa_check" CHECK ("tipo_pessoa" IN ('F', 'J'));
ALTER TABLE "cliente" ADD CONSTRAINT "cliente_uf_check" CHECK ("uf" IN (
  'AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA',
  'PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO'));

ALTER TABLE "servico" ADD CONSTRAINT "servico_valor_check" CHECK ("valor_referencia" >= 0);
ALTER TABLE "servico" ADD CONSTRAINT "servico_prazo_check" CHECK ("prazo_padrao_dias" > 0);

-- RNF09: arquivo de ate 10 mb
ALTER TABLE "documento" ADD CONSTRAINT "documento_tamanho_check" CHECK ("tamanho_bytes" > 0 AND "tamanho_bytes" <= 10485760);
ALTER TABLE "documento" ADD CONSTRAINT "documento_datas_check"
  CHECK ("data_validade" IS NULL OR "data_emissao" <= "data_validade");

ALTER TABLE "contrato" ADD CONSTRAINT "contrato_datas_check" CHECK ("data_fim" > "data_inicio");
ALTER TABLE "contrato" ADD CONSTRAINT "contrato_valor_check" CHECK ("valor" >= 0);

ALTER TABLE "historico_situacao" ADD CONSTRAINT "historico_situacao_nova_check"
  CHECK ("situacao_nova" IN ('ativo', 'pendente', 'bloqueado', 'inativo'));
ALTER TABLE "historico_situacao" ADD CONSTRAINT "historico_situacao_anterior_check"
  CHECK ("situacao_anterior" IS NULL OR "situacao_anterior" IN ('ativo', 'pendente', 'bloqueado', 'inativo'));
ALTER TABLE "historico_situacao" ADD CONSTRAINT "historico_motivo_check" CHECK (length("motivo") >= 10);

-- RN05: os valores possiveis do status. a sequencia entre eles fica na aplicacao
ALTER TABLE "ordem_servico" ADD CONSTRAINT "ordem_status_check"
  CHECK ("status" IN ('aberta', 'atribuida', 'em_execucao', 'concluida', 'cancelada'));
ALTER TABLE "ordem_servico" ADD CONSTRAINT "ordem_prioridade_check"
  CHECK ("prioridade" IN ('baixa', 'normal', 'alta', 'urgente'));
ALTER TABLE "ordem_servico" ADD CONSTRAINT "ordem_descricao_check" CHECK (length("descricao") >= 20);
ALTER TABLE "ordem_servico" ADD CONSTRAINT "ordem_prazo_check" CHECK ("prazo" >= "data_abertura"::date);
-- RN07: cancelamento com motivo de pelo menos 10 caracteres
ALTER TABLE "ordem_servico" ADD CONSTRAINT "ordem_motivo_cancelamento_check"
  CHECK ("motivo_cancelamento" IS NULL OR length("motivo_cancelamento") >= 10);

ALTER TABLE "andamento_ordem" ADD CONSTRAINT "andamento_status_novo_check"
  CHECK ("status_novo" IN ('aberta', 'atribuida', 'em_execucao', 'concluida', 'cancelada'));
ALTER TABLE "andamento_ordem" ADD CONSTRAINT "andamento_status_anterior_check"
  CHECK ("status_anterior" IS NULL OR "status_anterior" IN ('aberta', 'atribuida', 'em_execucao', 'concluida', 'cancelada'));

ALTER TABLE "avaliacao" ADD CONSTRAINT "avaliacao_nota_check" CHECK ("nota" BETWEEN 1 AND 5);

ALTER TABLE "log_acao" ADD CONSTRAINT "log_acao_check"
  CHECK ("acao" IN ('alteracao_situacao', 'atribuicao', 'cancelamento'));

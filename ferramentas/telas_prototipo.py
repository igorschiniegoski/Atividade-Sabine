# -*- coding: utf-8 -*-
"""
conteudo das telas do prototipo. o gerar-prototipo.py cuida da casca (cabecalho,
menu e rodape), aqui fica so o miolo de cada tela.

os dados sao ficticios, como exige a restricao de LGPD definida na 1a entrega.
a data de referencia usada nos exemplos é 22/09/2026.
"""

# ---------------------------------------------------------------- T01

LOGIN = """<div class="caixa-login">
  <div class="marca-login">
    <strong>SGP</strong>
    <span>Gestão de prestadores de serviço</span>
  </div>

  <div class="cartao">
    <div class="cartao-corpo">
      <div class="campo largo">
        <label>E-mail</label>
        <input type="email" value="rosangela.dias@predialmga.com.br">
      </div>
      <div class="campo largo com-erro" style="margin-bottom:8px">
        <label>Senha</label>
        <input type="password" value="············">
        <span class="erro">E-mail ou senha inválidos.</span>
      </div>
      <a class="btn btn-primario" style="width:100%;text-align:center" href="T02-painel-administrador.html">Entrar</a>
    </div>
  </div>

  <p class="rodape-login">
    No protótipo os três perfis ficam abertos:
    <a href="T02-painel-administrador.html">administrador</a>,
    <a href="T13-minhas-ordens.html">prestador</a> ou
    <a href="T16-minhas-solicitacoes.html">cliente</a>.
    <br><a href="index.html">Ver o mapa das telas</a>
  </p>
</div>"""

# ---------------------------------------------------------------- T02

PAINEL_ADM = """<div class="indicadores">
  <a class="indicador alerta" href="T10-vencimentos.html">
    <div class="rotulo">Documentos vencidos</div>
    <div class="numero">3</div>
    <div class="detalhe">2 prestadores bloqueados</div>
  </a>
  <a class="indicador atencao" href="T10-vencimentos.html">
    <div class="rotulo">Vencem em 30 dias</div>
    <div class="numero">5</div>
    <div class="detalhe">o mais próximo em 6 dias</div>
  </a>
  <a class="indicador" href="T11-ordens.html">
    <div class="rotulo">Ordens aguardando atribuição</div>
    <div class="numero">4</div>
    <div class="detalhe">1 com prazo para amanhã</div>
  </a>
  <a class="indicador ok" href="T11-ordens.html">
    <div class="rotulo">Concluídas no mês</div>
    <div class="numero">27</div>
    <div class="detalhe">92% dentro do prazo</div>
  </a>
</div>

<div class="cartao">
  <h2>Ordens que precisam de ação</h2>
  <table>
    <thead>
      <tr><th>Número</th><th>Cliente</th><th>Serviço</th><th>Prazo</th><th>Situação</th><th class="acoes">&nbsp;</th></tr>
    </thead>
    <tbody>
      <tr>
        <td data-rotulo="Número">OS-2026-0147</td>
        <td data-rotulo="Cliente">Padaria Dom Bosco</td>
        <td data-rotulo="Serviço">Desentupimento de pia<span class="secundario">Hidráulica</span></td>
        <td data-rotulo="Prazo">23/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-aberta">Aberta</span></td>
        <td class="acoes"><a class="btn btn-primario btn-pequeno" href="T12-ordem-administrador.html">Atribuir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Número">OS-2026-0149</td>
        <td data-rotulo="Cliente">Colégio São Vicente</td>
        <td data-rotulo="Serviço">Troca de disjuntor<span class="secundario">Elétrica</span></td>
        <td data-rotulo="Prazo">26/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-aberta">Aberta</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T12-ordem-administrador.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Número">OS-2026-0148</td>
        <td data-rotulo="Cliente">Supermercado Zanin</td>
        <td data-rotulo="Serviço">Instalação de tomadas<span class="secundario">Elétrica</span></td>
        <td data-rotulo="Prazo">24/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-execucao">Em execução</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T12-ordem-administrador.html">Abrir</a></td>
      </tr>
    </tbody>
  </table>
</div>

<div class="cartao">
  <h2>Documentação em risco</h2>
  <table>
    <thead>
      <tr><th>Prestador</th><th>Documento</th><th>Validade</th><th>Situação</th><th class="acoes">&nbsp;</th></tr>
    </thead>
    <tbody>
      <tr>
        <td data-rotulo="Prestador">José Carlos de Oliveira</td>
        <td data-rotulo="Documento">Certidão negativa de débitos</td>
        <td data-rotulo="Validade">12/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-vencido">Vencido há 10 dias</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04c-prestador-documentos.html">Ver cadastro</a></td>
      </tr>
      <tr>
        <td data-rotulo="Prestador">Polar Refrigeração</td>
        <td data-rotulo="Documento">Apólice de seguro</td>
        <td data-rotulo="Validade">28/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-vence">Vence em 6 dias</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04c-prestador-documentos.html">Ver cadastro</a></td>
      </tr>
    </tbody>
  </table>
</div>"""

# ---------------------------------------------------------------- T03

PRESTADORES = """<div class="cartao">
  <div class="cartao-corpo">
    <div class="linha">
      <div class="campo">
        <label>Buscar</label>
        <input type="text" placeholder="Nome, razão social, CPF ou CNPJ">
      </div>
      <div class="campo estreito">
        <label>Situação</label>
        <select><option>Todas</option><option>Ativo</option><option>Pendente</option><option>Bloqueado</option><option>Inativo</option></select>
      </div>
      <div class="campo estreito">
        <label>Categoria</label>
        <select><option>Todas</option><option>Elétrica</option><option>Hidráulica</option><option>Limpeza</option><option>Refrigeração</option></select>
      </div>
      <div class="campo estreito" style="display:flex;align-items:flex-end">
        <a class="btn btn-neutro" href="T03-prestadores.html">Filtrar</a>
      </div>
    </div>
  </div>
</div>

<div class="cartao">
  <h2>5 prestadores encontrados</h2>
  <table>
    <thead>
      <tr><th>Prestador</th><th>CPF / CNPJ</th><th>Categorias</th><th>Situação</th><th class="numerico">Nota</th><th class="acoes">&nbsp;</th></tr>
    </thead>
    <tbody>
      <tr>
        <td data-rotulo="Prestador">ELETRICA SANTOS E CIA LTDA<span class="secundario">Elétrica Santos, (44) 99812-4410</span></td>
        <td data-rotulo="CNPJ">07.412.865/0001-34</td>
        <td data-rotulo="Categorias">Elétrica</td>
        <td data-rotulo="Situação"><span class="chip chip-ativo">Ativo</span></td>
        <td class="numerico" data-rotulo="Nota">4,8</td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04-prestador-dados.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Prestador">JOSE CARLOS DE OLIVEIRA<span class="secundario">autônomo, (44) 99745-2201</span></td>
        <td data-rotulo="CPF">041.288.376-52</td>
        <td data-rotulo="Categorias">Hidráulica</td>
        <td data-rotulo="Situação"><span class="chip chip-pendente">Pendente</span></td>
        <td class="numerico" data-rotulo="Nota">4,2</td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04-prestador-dados.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Prestador">LIMPADORA SAO JUDAS LTDA<span class="secundario">São Judas, (44) 3025-7788</span></td>
        <td data-rotulo="CNPJ">19.603.774/0001-08</td>
        <td data-rotulo="Categorias">Limpeza</td>
        <td data-rotulo="Situação"><span class="chip chip-ativo">Ativo</span></td>
        <td class="numerico" data-rotulo="Nota">4,5</td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04-prestador-dados.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Prestador">POLAR REFRIGERACAO E CLIMATIZACAO LTDA<span class="secundario">Polar, (44) 99120-3377</span></td>
        <td data-rotulo="CNPJ">26.155.908/0001-71</td>
        <td data-rotulo="Categorias">Refrigeração</td>
        <td data-rotulo="Situação"><span class="chip chip-bloqueado">Bloqueado</span></td>
        <td class="numerico" data-rotulo="Nota">Sem histórico</td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04-prestador-dados.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Prestador">VALDIR APARECIDO DA SILVA<span class="secundario">autônomo, 44 99666-1180</span></td>
        <td data-rotulo="CPF">883.041.529-15</td>
        <td data-rotulo="Categorias">Manutenção predial, Elétrica</td>
        <td data-rotulo="Situação"><span class="chip chip-ativo">Ativo</span></td>
        <td class="numerico" data-rotulo="Nota">3,9</td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04-prestador-dados.html">Abrir</a></td>
      </tr>
    </tbody>
  </table>
</div>"""

# ------------------------------------------------------ T04 (4 abas)

def abas_prestador(ativa):
    itens = [
        ("T04-prestador-dados.html", "Dados cadastrais"),
        ("T04b-prestador-categorias.html", "Categorias"),
        ("T04c-prestador-documentos.html", "Documentos"),
        ("T04d-prestador-situacao.html", "Situação cadastral"),
    ]
    return '<div class="abas">%s</div>' % "".join(
        '<a class="aba%s" href="%s">%s</a>' % (" ativa" if a == ativa else "", a, r)
        for a, r in itens
    )


PRESTADOR_DADOS = abas_prestador("T04-prestador-dados.html") + """
<div class="cartao">
  <h2>Identificação</h2>
  <div class="cartao-corpo">
    <div class="linha">
      <div class="campo estreito">
        <label>Tipo <span class="obrigatorio">*</span></label>
        <select><option>Pessoa jurídica</option><option>Pessoa física</option></select>
      </div>
      <div class="campo">
        <label>Razão social <span class="obrigatorio">*</span></label>
        <input type="text" value="ELETRICA SANTOS E CIA LTDA">
      </div>
      <div class="campo com-erro">
        <label>CNPJ <span class="obrigatorio">*</span></label>
        <input type="text" value="07.412.865/0001-00">
        <span class="erro">CNPJ inválido: o dígito verificador não confere.</span>
      </div>
    </div>
    <div class="linha">
      <div class="campo">
        <label>Telefone <span class="obrigatorio">*</span></label>
        <input type="text" value="(44) 99812-4410">
      </div>
      <div class="campo">
        <label>E-mail</label>
        <input type="email" value="eletricasantos@hotmail.com">
        <span class="ajuda">Usado também para liberar o acesso do prestador ao sistema.</span>
      </div>
    </div>
  </div>
</div>

<div class="cartao">
  <h2>Endereço</h2>
  <div class="cartao-corpo">
    <div class="linha">
      <div class="campo estreito">
        <label>CEP <span class="obrigatorio">*</span></label>
        <input type="text" value="87020-025">
      </div>
      <div class="campo">
        <label>Logradouro <span class="obrigatorio">*</span></label>
        <input type="text" value="Avenida Brasil">
      </div>
      <div class="campo estreito">
        <label>Número <span class="obrigatorio">*</span></label>
        <input type="text" value="1420">
      </div>
      <div class="campo estreito">
        <label>Complemento</label>
        <input type="text" value="Sala 3">
      </div>
    </div>
    <div class="linha">
      <div class="campo">
        <label>Bairro <span class="obrigatorio">*</span></label>
        <input type="text" value="Centro">
      </div>
      <div class="campo">
        <label>Cidade <span class="obrigatorio">*</span></label>
        <input type="text" value="Maringá">
      </div>
      <div class="campo estreito">
        <label>UF <span class="obrigatorio">*</span></label>
        <select><option>PR</option><option>SP</option><option>SC</option></select>
      </div>
    </div>
  </div>
  <div class="rodape-form">
    <a class="btn btn-neutro" href="T03-prestadores.html">Cancelar</a>
    <a class="btn btn-primario" href="T03-prestadores.html">Salvar</a>
  </div>
</div>"""

PRESTADOR_CATEGORIAS = abas_prestador("T04b-prestador-categorias.html") + """
<div class="aviso">
  <div>
    <strong>O prestador só aparece na atribuição das categorias marcadas aqui.</strong>
    É o que a regra RN04 exige: a ordem de serviço só pode ir para quem está habilitado na categoria do serviço.
  </div>
</div>

<div class="cartao">
  <h2>Categorias em que atua</h2>
  <div class="cartao-corpo">
    <div class="marcadores">
      <label class="marcador"><input type="checkbox" checked> Elétrica</label>
      <label class="marcador"><input type="checkbox"> Hidráulica</label>
      <label class="marcador"><input type="checkbox"> Limpeza</label>
      <label class="marcador"><input type="checkbox"> Manutenção predial</label>
      <label class="marcador"><input type="checkbox"> Refrigeração</label>
      <label class="marcador"><input type="checkbox"> Informática</label>
    </div>
  </div>
  <div class="rodape-form">
    <a class="btn btn-neutro" href="T03-prestadores.html">Cancelar</a>
    <a class="btn btn-primario" href="T04b-prestador-categorias.html">Salvar habilitações</a>
  </div>
</div>

<div class="cartao">
  <h2>Habilitações registradas</h2>
  <table>
    <thead><tr><th>Categoria</th><th>Habilitado em</th><th>Ordens concluídas</th></tr></thead>
    <tbody>
      <tr><td data-rotulo="Categoria">Elétrica</td><td data-rotulo="Habilitado em">03/02/2026</td><td data-rotulo="Ordens">31</td></tr>
    </tbody>
  </table>
</div>"""

PRESTADOR_DOCUMENTOS = abas_prestador("T04c-prestador-documentos.html") + """
<div class="aviso atencao">
  <div>
    <strong>Este prestador tem 1 documento obrigatório vencido.</strong>
    Enquanto não for regularizado, ele fica com situação pendente e não aparece na lista de atribuição (RN02).
  </div>
</div>

<div class="cartao">
  <h2>Documentos enviados</h2>
  <table>
    <thead>
      <tr><th>Tipo</th><th>Arquivo</th><th>Emissão</th><th>Validade</th><th>Situação</th><th class="acoes">&nbsp;</th></tr>
    </thead>
    <tbody>
      <tr>
        <td data-rotulo="Tipo">Certidão negativa de débitos<span class="secundario">Obrigatório</span></td>
        <td data-rotulo="Arquivo">cnd-2026.pdf<span class="secundario">312 KB</span></td>
        <td data-rotulo="Emissão">12/03/2026</td>
        <td data-rotulo="Validade">12/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-vencido">Vencido há 10 dias</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04c-prestador-documentos.html">Baixar</a></td>
      </tr>
      <tr>
        <td data-rotulo="Tipo">CNPJ<span class="secundario">Obrigatório</span></td>
        <td data-rotulo="Arquivo">cartao-cnpj.pdf<span class="secundario">180 KB</span></td>
        <td data-rotulo="Emissão">10/01/2026</td>
        <td data-rotulo="Validade">Não expira</td>
        <td data-rotulo="Situação"><span class="chip chip-ativo">Em dia</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04c-prestador-documentos.html">Baixar</a></td>
      </tr>
      <tr>
        <td data-rotulo="Tipo">Apólice de seguro</td>
        <td data-rotulo="Arquivo">apolice-2026.pdf<span class="secundario">1,2 MB</span></td>
        <td data-rotulo="Emissão">02/02/2026</td>
        <td data-rotulo="Validade">02/02/2027</td>
        <td data-rotulo="Situação"><span class="chip chip-ativo">Em dia</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04c-prestador-documentos.html">Baixar</a></td>
      </tr>
      <tr>
        <td data-rotulo="Tipo">Certidão negativa de débitos<span class="secundario">Versão anterior</span></td>
        <td data-rotulo="Arquivo">cnd-2025.pdf<span class="secundario">298 KB</span></td>
        <td data-rotulo="Emissão">15/09/2025</td>
        <td data-rotulo="Validade">15/03/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-neutro">Substituído</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04c-prestador-documentos.html">Baixar</a></td>
      </tr>
    </tbody>
  </table>
</div>"""

PRESTADOR_SITUACAO = abas_prestador("T04d-prestador-situacao.html") + """
<div class="colunas">
  <div class="cartao">
    <h2>Alterar situação cadastral</h2>
    <div class="cartao-corpo">
      <div class="campo largo">
        <label>Situação atual</label>
        <p style="margin:0"><span class="chip chip-pendente">Pendente</span></p>
      </div>
      <div class="campo largo">
        <label>Nova situação <span class="obrigatorio">*</span></label>
        <select><option>Ativo</option><option>Pendente</option><option>Bloqueado</option><option>Inativo</option></select>
      </div>
      <div class="campo largo">
        <label>Motivo <span class="obrigatorio">*</span></label>
        <textarea placeholder="Descreva o motivo da alteração"></textarea>
        <span class="ajuda">Mínimo de 10 caracteres. O motivo fica registrado no histórico e no log (RF19).</span>
      </div>
    </div>
    <div class="rodape-form">
      <a class="btn btn-neutro" href="T03-prestadores.html">Cancelar</a>
      <a class="btn btn-primario" href="T04d-prestador-situacao.html">Gravar alteração</a>
    </div>
  </div>

  <div class="cartao">
    <h2>Histórico de situação</h2>
    <div class="cartao-corpo">
      <ul class="tempo">
        <li>
          <strong>Ativo para pendente</strong>
          <span class="quando">13/09/2026 às 00:05, pelo sistema</span>
          Documento obrigatório vencido: certidão negativa de débitos (RN02).
        </li>
        <li>
          <strong>Pendente para ativo</strong>
          <span class="quando">14/03/2026 às 09:12, por Rosangela Dias</span>
          Documentação regularizada após envio da nova certidão.
        </li>
        <li>
          <strong>Cadastro criado como pendente</strong>
          <span class="quando">03/02/2026 às 14:40, por Rosangela Dias</span>
          Aguardando envio da documentação obrigatória.
        </li>
      </ul>
    </div>
  </div>
</div>"""

# ---------------------------------------------------------------- T05

CLIENTES = """<div class="cartao">
  <div class="cartao-corpo">
    <div class="linha">
      <div class="campo">
        <label>Buscar</label>
        <input type="text" placeholder="Nome, razão social, CPF ou CNPJ">
      </div>
      <div class="campo estreito">
        <label>Situação</label>
        <select><option>Ativos</option><option>Inativos</option><option>Todos</option></select>
      </div>
      <div class="campo estreito" style="display:flex;align-items:flex-end">
        <a class="btn btn-neutro" href="T05-clientes.html">Filtrar</a>
      </div>
    </div>
  </div>
</div>

<div class="cartao">
  <h2>4 clientes encontrados</h2>
  <table>
    <thead>
      <tr><th>Cliente</th><th>CPF / CNPJ</th><th>Cidade</th><th>Ordens abertas</th><th>Situação</th><th class="acoes">&nbsp;</th></tr>
    </thead>
    <tbody>
      <tr>
        <td data-rotulo="Cliente">ZANIN COMERCIO DE ALIMENTOS LTDA<span class="secundario">Supermercado Zanin, compras@superzanin.com.br</span></td>
        <td data-rotulo="CNPJ">05.937.612/0001-29</td>
        <td data-rotulo="Cidade">Maringá / PR</td>
        <td data-rotulo="Ordens abertas">2</td>
        <td data-rotulo="Situação"><span class="chip chip-ativo">Ativo</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T06-cliente-cadastro.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Cliente">PANIFICADORA DOM BOSCO LTDA<span class="secundario">Padaria Dom Bosco, padariadombosco@gmail.com</span></td>
        <td data-rotulo="CNPJ">22.804.157/0001-60</td>
        <td data-rotulo="Cidade">Maringá / PR</td>
        <td data-rotulo="Ordens abertas">1</td>
        <td data-rotulo="Situação"><span class="chip chip-ativo">Ativo</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T06-cliente-cadastro.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Cliente">Colégio São Vicente<span class="secundario">secretaria@saovicente.com.br</span></td>
        <td data-rotulo="CNPJ">31.470.286/0001-95</td>
        <td data-rotulo="Cidade">Sarandi / PR</td>
        <td data-rotulo="Ordens abertas">1</td>
        <td data-rotulo="Situação"><span class="chip chip-ativo">Ativo</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T06-cliente-cadastro.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Cliente">Auto Posto Maringá<span class="secundario">adm@autopostomga.com.br</span></td>
        <td data-rotulo="CNPJ">14.628.093/0001-47</td>
        <td data-rotulo="Cidade">Maringá / PR</td>
        <td data-rotulo="Ordens abertas">0</td>
        <td data-rotulo="Situação"><span class="chip chip-inativo">Inativo</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T06-cliente-cadastro.html">Abrir</a></td>
      </tr>
    </tbody>
  </table>
</div>"""

# ---------------------------------------------------------------- T06

CLIENTE_CADASTRO = """<div class="cartao">
  <h2>Identificação</h2>
  <div class="cartao-corpo">
    <div class="linha">
      <div class="campo estreito">
        <label>Tipo <span class="obrigatorio">*</span></label>
        <select><option>Pessoa jurídica</option><option>Pessoa física</option></select>
      </div>
      <div class="campo">
        <label>Razão social <span class="obrigatorio">*</span></label>
        <input type="text" value="ZANIN COMERCIO DE ALIMENTOS LTDA">
      </div>
      <div class="campo">
        <label>CNPJ <span class="obrigatorio">*</span></label>
        <input type="text" value="05.937.612/0001-29">
        <span class="ajuda">Não pode existir outro cadastro ativo com o mesmo número (RN10).</span>
      </div>
    </div>
    <div class="linha">
      <div class="campo">
        <label>Telefone <span class="obrigatorio">*</span></label>
        <input type="text" value="(44) 3028-1100">
      </div>
      <div class="campo">
        <label>E-mail</label>
        <input type="email" value="compras@superzanin.com.br">
      </div>
    </div>
  </div>
</div>

<div class="cartao">
  <h2>Endereço</h2>
  <div class="cartao-corpo">
    <div class="linha">
      <div class="campo estreito">
        <label>CEP <span class="obrigatorio">*</span></label>
        <input type="text" value="87013-210">
      </div>
      <div class="campo">
        <label>Logradouro <span class="obrigatorio">*</span></label>
        <input type="text" value="Rua Néo Alves Martins">
      </div>
      <div class="campo estreito">
        <label>Número <span class="obrigatorio">*</span></label>
        <input type="text" value="2810">
      </div>
      <div class="campo">
        <label>Bairro <span class="obrigatorio">*</span></label>
        <input type="text" value="Zona 3">
      </div>
    </div>
  </div>
  <div class="rodape-form">
    <a class="btn btn-neutro" href="T05-clientes.html">Cancelar</a>
    <a class="btn btn-primario" href="T05-clientes.html">Salvar</a>
  </div>
</div>"""

# ---------------------------------------------------------------- T07

CATEGORIAS = """<div class="colunas">
  <div class="cartao">
    <h2>Categorias cadastradas</h2>
    <table>
      <thead><tr><th>Categoria</th><th>Serviços</th><th>Prestadores</th><th>Situação</th></tr></thead>
      <tbody>
        <tr><td data-rotulo="Categoria">Elétrica</td><td data-rotulo="Serviços">6</td><td data-rotulo="Prestadores">2</td><td data-rotulo="Situação"><span class="chip chip-ativo">Ativa</span></td></tr>
        <tr><td data-rotulo="Categoria">Hidráulica</td><td data-rotulo="Serviços">4</td><td data-rotulo="Prestadores">1</td><td data-rotulo="Situação"><span class="chip chip-ativo">Ativa</span></td></tr>
        <tr><td data-rotulo="Categoria">Limpeza</td><td data-rotulo="Serviços">3</td><td data-rotulo="Prestadores">1</td><td data-rotulo="Situação"><span class="chip chip-ativo">Ativa</span></td></tr>
        <tr><td data-rotulo="Categoria">Manutenção predial</td><td data-rotulo="Serviços">5</td><td data-rotulo="Prestadores">1</td><td data-rotulo="Situação"><span class="chip chip-ativo">Ativa</span></td></tr>
        <tr><td data-rotulo="Categoria">Refrigeração</td><td data-rotulo="Serviços">2</td><td data-rotulo="Prestadores">1</td><td data-rotulo="Situação"><span class="chip chip-ativo">Ativa</span></td></tr>
        <tr><td data-rotulo="Categoria">Informática</td><td data-rotulo="Serviços">0</td><td data-rotulo="Prestadores">0</td><td data-rotulo="Situação"><span class="chip chip-inativo">Inativa</span></td></tr>
      </tbody>
    </table>
  </div>

  <div class="cartao" style="flex:0 1 340px">
    <h2>Nova categoria</h2>
    <div class="cartao-corpo">
      <div class="campo largo">
        <label>Nome <span class="obrigatorio">*</span></label>
        <input type="text" placeholder="Ex.: Jardinagem">
        <span class="ajuda">O nome não pode se repetir.</span>
      </div>
      <div class="campo largo">
        <label>Descrição</label>
        <textarea placeholder="O que essa categoria abrange"></textarea>
      </div>
      <div class="campo largo">
        <label class="marcador"><input type="checkbox" checked> Categoria ativa</label>
      </div>
    </div>
    <div class="rodape-form">
      <a class="btn btn-primario" href="T07-categorias.html">Adicionar</a>
    </div>
  </div>
</div>"""

# ---------------------------------------------------------------- T08

SERVICOS = """<div class="cartao">
  <div class="cartao-corpo">
    <div class="linha">
      <div class="campo">
        <label>Buscar</label>
        <input type="text" placeholder="Nome do serviço">
      </div>
      <div class="campo estreito">
        <label>Categoria</label>
        <select><option>Todas</option><option>Elétrica</option><option>Hidráulica</option><option>Limpeza</option></select>
      </div>
      <div class="campo estreito" style="display:flex;align-items:flex-end">
        <a class="btn btn-neutro" href="T08-servicos.html">Filtrar</a>
      </div>
    </div>
  </div>
</div>

<div class="cartao">
  <h2>20 serviços no catálogo</h2>
  <table>
    <thead>
      <tr><th>Serviço</th><th>Categoria</th><th class="numerico">Valor de referência</th><th class="numerico">Prazo padrão</th><th>Situação</th><th class="acoes">&nbsp;</th></tr>
    </thead>
    <tbody>
      <tr>
        <td data-rotulo="Serviço">Instalação de tomadas</td>
        <td data-rotulo="Categoria">Elétrica</td>
        <td class="numerico" data-rotulo="Valor">R$ 187,50</td>
        <td class="numerico" data-rotulo="Prazo">3 dias</td>
        <td data-rotulo="Situação"><span class="chip chip-ativo">Ativo</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T09-servico-cadastro.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Serviço">Troca de disjuntor</td>
        <td data-rotulo="Categoria">Elétrica</td>
        <td class="numerico" data-rotulo="Valor">R$ 122,00</td>
        <td class="numerico" data-rotulo="Prazo">2 dias</td>
        <td data-rotulo="Situação"><span class="chip chip-ativo">Ativo</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T09-servico-cadastro.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Serviço">Desentupimento de pia</td>
        <td data-rotulo="Categoria">Hidráulica</td>
        <td class="numerico" data-rotulo="Valor">R$ 215,00</td>
        <td class="numerico" data-rotulo="Prazo">1 dia</td>
        <td data-rotulo="Situação"><span class="chip chip-ativo">Ativo</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T09-servico-cadastro.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Serviço">Limpeza pós-obra</td>
        <td data-rotulo="Categoria">Limpeza</td>
        <td class="numerico" data-rotulo="Valor">R$ 940,00</td>
        <td class="numerico" data-rotulo="Prazo">2 dias</td>
        <td data-rotulo="Situação"><span class="chip chip-ativo">Ativo</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T09-servico-cadastro.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Serviço">Manutenção de ar-condicionado</td>
        <td data-rotulo="Categoria">Refrigeração</td>
        <td class="numerico" data-rotulo="Valor">R$ 300,00</td>
        <td class="numerico" data-rotulo="Prazo">4 dias</td>
        <td data-rotulo="Situação"><span class="chip chip-ativo">Ativo</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T09-servico-cadastro.html">Abrir</a></td>
      </tr>
    </tbody>
  </table>
</div>"""

# ---------------------------------------------------------------- T09

SERVICO_CADASTRO = """<div class="cartao">
  <h2>Dados do serviço</h2>
  <div class="cartao-corpo">
    <div class="linha">
      <div class="campo">
        <label>Nome <span class="obrigatorio">*</span></label>
        <input type="text" value="Instalação de tomadas">
      </div>
      <div class="campo estreito">
        <label>Categoria <span class="obrigatorio">*</span></label>
        <select><option>Elétrica</option><option>Hidráulica</option><option>Limpeza</option><option>Refrigeração</option></select>
      </div>
    </div>
    <div class="campo largo">
      <label>Descrição</label>
      <textarea>Instalação de tomadas novas em alvenaria ou drywall, incluindo passagem de cabo e teste de carga. O material fica por conta do cliente.</textarea>
    </div>
    <div class="linha">
      <div class="campo estreito">
        <label>Valor de referência</label>
        <input type="text" value="187,50">
        <span class="ajuda">Serve de base para o orçamento, não é o valor cobrado.</span>
      </div>
      <div class="campo estreito">
        <label>Prazo padrão <span class="obrigatorio">*</span></label>
        <input type="text" value="3 dias">
        <span class="ajuda">Aplicado quando o cliente não informa prazo na solicitação.</span>
      </div>
      <div class="campo estreito">
        <label>Situação</label>
        <label class="marcador" style="margin-top:8px"><input type="checkbox" checked> Serviço ativo</label>
      </div>
    </div>
  </div>
  <div class="rodape-form">
    <a class="btn btn-neutro" href="T08-servicos.html">Cancelar</a>
    <a class="btn btn-primario" href="T08-servicos.html">Salvar</a>
  </div>
</div>"""

# ---------------------------------------------------------------- T10

VENCIMENTOS = """<div class="cartao">
  <h2>Vencidos (3)</h2>
  <table>
    <thead>
      <tr><th>Prestador</th><th>Documento</th><th>Validade</th><th>Atraso</th><th>Situação do prestador</th><th class="acoes">&nbsp;</th></tr>
    </thead>
    <tbody>
      <tr>
        <td data-rotulo="Prestador">José Carlos de Oliveira</td>
        <td data-rotulo="Documento">Certidão negativa de débitos</td>
        <td data-rotulo="Validade">12/09/2026</td>
        <td data-rotulo="Atraso">10 dias</td>
        <td data-rotulo="Situação"><span class="chip chip-pendente">Pendente</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04d-prestador-situacao.html">Alterar situação</a></td>
      </tr>
      <tr>
        <td data-rotulo="Prestador">Polar Refrigeração</td>
        <td data-rotulo="Documento">Certidão negativa de débitos</td>
        <td data-rotulo="Validade">30/08/2026</td>
        <td data-rotulo="Atraso">23 dias</td>
        <td data-rotulo="Situação"><span class="chip chip-bloqueado">Bloqueado</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04d-prestador-situacao.html">Alterar situação</a></td>
      </tr>
      <tr>
        <td data-rotulo="Prestador">Valdir Aparecido</td>
        <td data-rotulo="Documento">Certificado de curso NR-10</td>
        <td data-rotulo="Validade">18/09/2026</td>
        <td data-rotulo="Atraso">4 dias</td>
        <td data-rotulo="Situação"><span class="chip chip-pendente">Pendente</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04d-prestador-situacao.html">Alterar situação</a></td>
      </tr>
    </tbody>
  </table>
</div>

<div class="cartao">
  <h2>Vencem nos próximos 30 dias (5)</h2>
  <table>
    <thead>
      <tr><th>Prestador</th><th>Documento</th><th>Validade</th><th>Faltam</th><th class="acoes">&nbsp;</th></tr>
    </thead>
    <tbody>
      <tr>
        <td data-rotulo="Prestador">Polar Refrigeração</td>
        <td data-rotulo="Documento">Apólice de seguro</td>
        <td data-rotulo="Validade">28/09/2026</td>
        <td data-rotulo="Faltam"><span class="chip chip-vence">6 dias</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04c-prestador-documentos.html">Ver documentos</a></td>
      </tr>
      <tr>
        <td data-rotulo="Prestador">Limpadora São Judas</td>
        <td data-rotulo="Documento">Certidão negativa de débitos</td>
        <td data-rotulo="Validade">04/10/2026</td>
        <td data-rotulo="Faltam"><span class="chip chip-vence">12 dias</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04c-prestador-documentos.html">Ver documentos</a></td>
      </tr>
      <tr>
        <td data-rotulo="Prestador">Elétrica Santos</td>
        <td data-rotulo="Documento">Certificado de curso NR-10</td>
        <td data-rotulo="Validade">11/10/2026</td>
        <td data-rotulo="Faltam"><span class="chip chip-vence">19 dias</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T04c-prestador-documentos.html">Ver documentos</a></td>
      </tr>
    </tbody>
  </table>
</div>"""

# ---------------------------------------------------------------- T11

ORDENS = """<div class="cartao">
  <div class="cartao-corpo">
    <div class="linha">
      <div class="campo">
        <label>Buscar</label>
        <input type="text" placeholder="Número da ordem, cliente ou serviço">
      </div>
      <div class="campo estreito">
        <label>Situação</label>
        <select><option>Todas</option><option>Aberta</option><option>Atribuída</option><option>Em execução</option><option>Concluída</option><option>Cancelada</option></select>
      </div>
      <div class="campo estreito">
        <label>Período</label>
        <select><option>Últimos 30 dias</option><option>Este mês</option><option>Personalizado</option></select>
      </div>
      <div class="campo estreito" style="display:flex;align-items:flex-end">
        <a class="btn btn-neutro" href="T11-ordens.html">Filtrar</a>
      </div>
    </div>
  </div>
</div>

<div class="cartao">
  <h2>5 ordens no período</h2>
  <table>
    <thead>
      <tr><th>Número</th><th>Cliente</th><th>Serviço</th><th>Prestador</th><th>Prazo</th><th>Situação</th><th class="acoes">&nbsp;</th></tr>
    </thead>
    <tbody>
      <tr>
        <td data-rotulo="Número">OS-2026-0149</td>
        <td data-rotulo="Cliente">Colégio São Vicente</td>
        <td data-rotulo="Serviço">Troca de disjuntor</td>
        <td data-rotulo="Prestador"><span class="secundario">Não atribuída</span></td>
        <td data-rotulo="Prazo">26/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-aberta">Aberta</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T12-ordem-administrador.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Número">OS-2026-0148</td>
        <td data-rotulo="Cliente">Supermercado Zanin</td>
        <td data-rotulo="Serviço">Instalação de tomadas</td>
        <td data-rotulo="Prestador">Elétrica Santos</td>
        <td data-rotulo="Prazo">24/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-execucao">Em execução</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T12-ordem-administrador.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Número">OS-2026-0147</td>
        <td data-rotulo="Cliente">Padaria Dom Bosco</td>
        <td data-rotulo="Serviço">Desentupimento de pia</td>
        <td data-rotulo="Prestador"><span class="secundario">Não atribuída</span></td>
        <td data-rotulo="Prazo">23/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-aberta">Aberta</span></td>
        <td class="acoes"><a class="btn btn-primario btn-pequeno" href="T12-ordem-administrador.html">Atribuir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Número">OS-2026-0146</td>
        <td data-rotulo="Cliente">Colégio São Vicente</td>
        <td data-rotulo="Serviço">Limpeza pós-obra</td>
        <td data-rotulo="Prestador">Limpadora São Judas</td>
        <td data-rotulo="Prazo">16/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-concluida">Concluída</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T12-ordem-administrador.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Número">OS-2026-0145</td>
        <td data-rotulo="Cliente">Auto Posto Maringá</td>
        <td data-rotulo="Serviço">Manutenção de ar-condicionado</td>
        <td data-rotulo="Prestador"><span class="secundario">Não atribuída</span></td>
        <td data-rotulo="Prazo">12/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-cancelada">Cancelada</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T12-ordem-administrador.html">Abrir</a></td>
      </tr>
    </tbody>
  </table>
</div>"""

# ---------------------------------------------------------------- T12

ORDEM_ADM = """<div class="cartao">
  <div class="cartao-corpo">
    <div class="trilha">
      <span class="passo atual">Aberta</span>
      <span class="passo">Atribuída</span>
      <span class="passo">Em execução</span>
      <span class="passo">Concluída</span>
    </div>
    <p class="subtitulo" style="margin-bottom:0">A ordem só anda nessa sequência. Não é possível pular etapa nem voltar
    para um status anterior (RN05).</p>
  </div>
</div>

<div class="colunas">
  <div class="cartao">
    <h2>Dados da ordem</h2>
    <div class="cartao-corpo">
      <div class="linha">
        <div class="campo"><label>Cliente</label><p style="margin:0">Padaria Dom Bosco</p></div>
        <div class="campo"><label>Serviço</label><p style="margin:0">Desentupimento de pia<span class="secundario">Categoria: Hidráulica</span></p></div>
      </div>
      <div class="linha">
        <div class="campo"><label>Aberta em</label><p style="margin:0">21/09/2026 às 08:47</p></div>
        <div class="campo"><label>Prazo combinado</label><p style="margin:0">23/09/2026</p></div>
        <div class="campo"><label>Prioridade</label><p style="margin:0"><span class="chip chip-pendente">Alta</span></p></div>
      </div>
      <div class="campo largo">
        <label>Descrição do cliente</label>
        <p style="margin:0">a pia da cozinha entupiu ontem de tarde e a agua nao desce mais. ja transbordou uma vez
        e molhou o estoque de farinha. precisa resolver antes de quinta se nao a padaria nao abre</p>
      </div>
      <div class="campo largo">
        <label>Prestador responsável</label>
        <p style="margin:0">Ainda não atribuída<span class="secundario">Aberta há 1 dia, prazo em 23/09/2026</span></p>
      </div>
    </div>
    <div class="rodape-form">
      <a class="btn btn-perigo" href="T12c-cancelar-ordem.html">Cancelar ordem</a>
      <a class="btn btn-primario" href="T12b-atribuir-ordem.html">Atribuir prestador</a>
    </div>
  </div>

  <div class="cartao" style="flex:0 1 380px">
    <h2>Histórico da ordem</h2>
    <div class="cartao-corpo">
      <ul class="tempo">
        <li>
          <strong>Ordem aberta</strong>
          <span class="quando">21/09/2026 às 08:47, por Padaria Dom Bosco</span>
          Prazo desejado informado pelo cliente.
        </li>
      </ul>
    </div>
  </div>
</div>"""

# --------------------------------------------------------------- T12b

ATRIBUIR = """<div class="modal-fundo">
  <span class="rotulo-simulacao">Janela sobre a tela da ordem OS-2026-0147</span>
  <div class="modal">
    <h2>Atribuir a ordem a um prestador</h2>
    <div class="modal-corpo">
      <div class="aviso">
        <div>
          <strong>Aparecem apenas os prestadores aptos para esta ordem.</strong>
          Aptidão é estar ativo, estar habilitado na categoria Hidráulica e não ter documento obrigatório vencido
          (RN01, RN02 e RN04).
        </div>
      </div>

      <table>
        <thead><tr><th>Prestador</th><th class="numerico">Nota</th><th class="numerico">Ordens abertas</th><th class="acoes">&nbsp;</th></tr></thead>
        <tbody>
          <tr>
            <td data-rotulo="Prestador">HIDRAULICA TRES LAGOAS LTDA<span class="secundario">31 ordens concluídas, última em 08/09</span></td>
            <td class="numerico" data-rotulo="Nota">4,6</td>
            <td class="numerico" data-rotulo="Ordens">2</td>
            <td class="acoes"><a class="btn btn-primario btn-pequeno" href="T12-ordem-administrador.html">Atribuir</a></td>
          </tr>
          <tr>
            <td data-rotulo="Prestador">J R INSTALACOES HIDRAULICAS ME<span class="secundario">cadastrado em 02/09, 2 ordens concluídas</span></td>
            <td class="numerico" data-rotulo="Nota">Sem histórico suficiente</td>
            <td class="numerico" data-rotulo="Ordens">0</td>
            <td class="acoes"><a class="btn btn-primario btn-pequeno" href="T12-ordem-administrador.html">Atribuir</a></td>
          </tr>
        </tbody>
      </table>

      <h3 style="font-size:14px;margin:22px 0 6px">Não disponíveis para esta ordem</h3>
      <p class="subtitulo" style="margin-top:0">A lista abaixo evita a dúvida de por que um prestador conhecido não
      aparece. Nenhum deles pode ser selecionado.</p>
      <table>
        <thead><tr><th>Prestador</th><th>Motivo do impedimento</th></tr></thead>
        <tbody>
          <tr>
            <td data-rotulo="Prestador">José Carlos de Oliveira</td>
            <td data-rotulo="Motivo"><span class="chip chip-vencido">Documento vencido</span> Certidão negativa de débitos venceu em 12/09/2026</td>
          </tr>
          <tr>
            <td data-rotulo="Prestador">Polar Refrigeração</td>
            <td data-rotulo="Motivo"><span class="chip chip-bloqueado">Bloqueado</span> Situação cadastral não permite atribuição</td>
          </tr>
          <tr>
            <td data-rotulo="Prestador">Elétrica Santos</td>
            <td data-rotulo="Motivo"><span class="chip chip-neutro">Categoria</span> Não está habilitado em Hidráulica</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="rodape-form">
      <a class="btn btn-neutro" href="T11-ordens.html">Fechar</a>
    </div>
  </div>
</div>"""

# --------------------------------------------------------------- T12c

CANCELAR = """<div class="modal-fundo">
  <span class="rotulo-simulacao">Janela sobre a tela da ordem OS-2026-0147</span>
  <div class="modal">
    <h2>Cancelar a ordem OS-2026-0147</h2>
    <div class="modal-corpo">
      <div class="aviso atencao">
        <div>
          <strong>O cancelamento não apaga a ordem.</strong>
          Ela continua no histórico com o motivo registrado, e o evento vai para o log de auditoria (RF19).
        </div>
      </div>
      <div class="campo largo com-erro">
        <label>Motivo do cancelamento <span class="obrigatorio">*</span></label>
        <textarea>duplicada</textarea>
        <span class="erro">O motivo precisa ter no mínimo 10 caracteres. Faltam 1.</span>
        <span class="ajuda">Regra RN07. Ordens já concluídas não podem ser canceladas (RN06).</span>
      </div>
    </div>
    <div class="rodape-form">
      <a class="btn btn-neutro" href="T12-ordem-administrador.html">Voltar</a>
      <a class="btn btn-perigo" href="T12c-cancelar-ordem.html" aria-disabled="true">Confirmar cancelamento</a>
    </div>
  </div>
</div>"""

# ---------------------------------------------------------------- T13

MINHAS_ORDENS = """<div class="indicadores">
  <a class="indicador" href="T14-ordem-execucao.html">
    <div class="rotulo">Atribuídas a mim</div>
    <div class="numero">1</div>
    <div class="detalhe">aguardando início</div>
  </a>
  <a class="indicador atencao" href="T14-ordem-execucao.html">
    <div class="rotulo">Em execução</div>
    <div class="numero">1</div>
    <div class="detalhe">prazo em 2 dias</div>
  </a>
  <a class="indicador ok" href="T13-minhas-ordens.html">
    <div class="rotulo">Concluídas no mês</div>
    <div class="numero">9</div>
    <div class="detalhe">todas dentro do prazo</div>
  </a>
</div>

<div class="cartao">
  <h2>Ordens atribuídas a mim</h2>
  <table>
    <thead>
      <tr><th>Número</th><th>Cliente</th><th>Serviço</th><th>Prazo</th><th>Situação</th><th class="acoes">&nbsp;</th></tr>
    </thead>
    <tbody>
      <tr>
        <td data-rotulo="Número">OS-2026-0148</td>
        <td data-rotulo="Cliente">Supermercado Zanin</td>
        <td data-rotulo="Serviço">Instalação de tomadas</td>
        <td data-rotulo="Prazo">24/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-execucao">Em execução</span></td>
        <td class="acoes"><a class="btn btn-primario btn-pequeno" href="T14-ordem-execucao.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Número">OS-2026-0150</td>
        <td data-rotulo="Cliente">Colégio São Vicente</td>
        <td data-rotulo="Serviço">Troca de disjuntor</td>
        <td data-rotulo="Prazo">26/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-atribuida">Atribuída</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T14-ordem-execucao.html">Abrir</a></td>
      </tr>
      <tr>
        <td data-rotulo="Número">OS-2026-0144</td>
        <td data-rotulo="Cliente">Supermercado Zanin</td>
        <td data-rotulo="Serviço">Troca de disjuntor</td>
        <td data-rotulo="Prazo">15/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-concluida">Concluída</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T14-ordem-execucao.html">Abrir</a></td>
      </tr>
    </tbody>
  </table>
</div>

<div class="cartao">
  <h2>Ordens de outros prestadores</h2>
  <div class="vazio">
    <strong>Esta lista não existe para o seu perfil</strong>
    O prestador enxerga apenas as ordens atribuídas a ele. O recorte é feito no servidor, não escondendo a informação
    na tela (RNF02).
  </div>
</div>"""

# ---------------------------------------------------------------- T14

ORDEM_EXECUCAO = """<div class="cartao">
  <div class="cartao-corpo">
    <div class="trilha">
      <span class="passo feito">Aberta</span><span class="passo feito">Atribuída</span><span class="passo atual">Em execução</span><span class="passo">Concluída</span>
    </div>
  </div>
</div>

<div class="colunas">
  <div class="cartao">
    <h2>O que foi pedido</h2>
    <div class="cartao-corpo">
      <div class="linha">
        <div class="campo"><label>Cliente</label><p style="margin:0">Supermercado Zanin<span class="secundario">Rua Néo Alves Martins, 2810 - Zona 3</span></p></div>
        <div class="campo"><label>Prazo</label><p style="margin:0">24/09/2026<span class="secundario">faltam 2 dias</span></p></div>
      </div>
      <div class="campo largo">
        <label>Descrição</label>
        <p style="margin:0">instalar 4 tomadas no estoque, 2 em cada parede. uma delas tem que ser de 20A por causa
        da seladora nova. o material ja comprei, esta na sala do gerente</p>
      </div>
    </div>
  </div>

  <div class="cartao" style="flex:0 1 400px">
    <h2>Registrar andamento</h2>
    <div class="cartao-corpo">
      <div class="campo largo">
        <label>Observação</label>
        <textarea placeholder="O que foi feito até agora">passei o cabo das duas primeiras tomadas. amanha volto pra fechar a parede</textarea>
        <span class="ajuda">O cliente e o administrador enxergam esse registro.</span>
      </div>
      <a class="btn btn-neutro" href="T14-ordem-execucao.html">Salvar andamento</a>
    </div>
  </div>
</div>

<div class="cartao">
  <h2>Concluir o serviço</h2>
  <div class="cartao-corpo">
    <div class="campo largo com-erro">
      <label>Relato do que foi executado <span class="obrigatorio">*</span></label>
      <textarea placeholder="Descreva o que foi executado"></textarea>
      <span class="erro">Descreva o que foi executado antes de concluir a ordem.</span>
      <span class="ajuda">Depois de concluída, a ordem não pode mais ser alterada (RN06). A correção exige
      cancelamento com justificativa e abertura de uma nova ordem.</span>
    </div>
  </div>
  <div class="rodape-form">
    <a class="btn btn-neutro" href="T13-minhas-ordens.html">Voltar</a>
    <a class="btn btn-primario" href="T13-minhas-ordens.html">Concluir ordem</a>
  </div>
</div>

<div class="cartao">
  <h2>Histórico</h2>
  <div class="cartao-corpo">
    <ul class="tempo">
      <li><strong>Execução iniciada</strong><span class="quando">22/09/2026 às 10:02, por Elétrica Santos</span></li>
      <li><strong>Ordem atribuída</strong><span class="quando">21/09/2026 às 16:30, por Rosangela Dias</span></li>
      <li><strong>Ordem aberta</strong><span class="quando">21/09/2026 às 15:58, por Supermercado Zanin</span></li>
    </ul>
  </div>
</div>"""

# ---------------------------------------------------------------- T15

MEUS_DOCUMENTOS = """<div class="aviso atencao">
  <div>
    <strong>Um documento obrigatório está para vencer.</strong>
    O certificado de curso NR-10 vence em 11/10/2026. Documento vencido tira o prestador da lista de atribuição até a
    regularização (RN02).
  </div>
</div>

<div class="colunas">
  <div class="cartao">
    <h2>Documentos enviados</h2>
    <table>
      <thead><tr><th>Tipo</th><th>Validade</th><th>Situação</th></tr></thead>
      <tbody>
        <tr><td data-rotulo="Tipo">CNPJ</td><td data-rotulo="Validade">Não expira</td><td data-rotulo="Situação"><span class="chip chip-ativo">Em dia</span></td></tr>
        <tr><td data-rotulo="Tipo">Certidão negativa de débitos</td><td data-rotulo="Validade">20/12/2026</td><td data-rotulo="Situação"><span class="chip chip-ativo">Em dia</span></td></tr>
        <tr><td data-rotulo="Tipo">Apólice de seguro</td><td data-rotulo="Validade">02/02/2027</td><td data-rotulo="Situação"><span class="chip chip-ativo">Em dia</span></td></tr>
        <tr><td data-rotulo="Tipo">Certificado de curso NR-10</td><td data-rotulo="Validade">11/10/2026</td><td data-rotulo="Situação"><span class="chip chip-vence">Vence em 19 dias</span></td></tr>
      </tbody>
    </table>
  </div>

  <div class="cartao" style="flex:0 1 380px">
    <h2>Enviar documento</h2>
    <div class="cartao-corpo">
      <div class="campo largo">
        <label>Tipo <span class="obrigatorio">*</span></label>
        <select><option>Certificado de curso NR-10</option><option>Certidão negativa de débitos</option><option>Apólice de seguro</option><option>CNPJ</option></select>
      </div>
      <div class="linha">
        <div class="campo">
          <label>Data de emissão <span class="obrigatorio">*</span></label>
          <input type="text" value="12/10/2026">
        </div>
        <div class="campo">
          <label>Validade <span class="obrigatorio">*</span></label>
          <input type="text" value="11/10/2027">
        </div>
      </div>
      <div class="campo largo com-erro">
        <label>Arquivo <span class="obrigatorio">*</span></label>
        <input type="text" value="certificado-nr10.docx">
        <span class="erro">Formato não aceito. Envie o arquivo em PDF, JPG ou PNG, com até 10 MB.</span>
      </div>
    </div>
    <div class="rodape-form">
      <a class="btn btn-primario" href="T15-meus-documentos.html">Enviar</a>
    </div>
  </div>
</div>"""

# ---------------------------------------------------------------- T16

MINHAS_SOLICITACOES = """<div class="cartao">
  <h2>Minhas solicitações</h2>
  <table>
    <thead>
      <tr><th>Número</th><th>Serviço</th><th>Aberta em</th><th>Prazo</th><th>Situação</th><th class="acoes">&nbsp;</th></tr>
    </thead>
    <tbody>
      <tr>
        <td data-rotulo="Número">OS-2026-0148</td>
        <td data-rotulo="Serviço">Instalação de tomadas</td>
        <td data-rotulo="Aberta em">21/09/2026</td>
        <td data-rotulo="Prazo">24/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-execucao">Em execução</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T18-ordem-cliente.html">Acompanhar</a></td>
      </tr>
      <tr>
        <td data-rotulo="Número">OS-2026-0144</td>
        <td data-rotulo="Serviço">Troca de disjuntor</td>
        <td data-rotulo="Aberta em">12/09/2026</td>
        <td data-rotulo="Prazo">15/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-concluida">Concluída</span></td>
        <td class="acoes"><a class="btn btn-primario btn-pequeno" href="T18-ordem-cliente.html">Avaliar</a></td>
      </tr>
      <tr>
        <td data-rotulo="Número">OS-2026-0139</td>
        <td data-rotulo="Serviço">Limpeza pós-obra</td>
        <td data-rotulo="Aberta em">28/08/2026</td>
        <td data-rotulo="Prazo">01/09/2026</td>
        <td data-rotulo="Situação"><span class="chip chip-concluida">Concluída</span></td>
        <td class="acoes"><a class="btn btn-neutro btn-pequeno" href="T18-ordem-cliente.html">Ver avaliação</a></td>
      </tr>
    </tbody>
  </table>
</div>"""

# ---------------------------------------------------------------- T17

NOVA_SOLICITACAO = """<div class="cartao">
  <h2>O que você precisa</h2>
  <div class="cartao-corpo">
    <div class="linha">
      <div class="campo">
        <label>Categoria <span class="obrigatorio">*</span></label>
        <select><option>Elétrica</option><option>Hidráulica</option><option>Limpeza</option><option>Refrigeração</option></select>
      </div>
      <div class="campo">
        <label>Serviço <span class="obrigatorio">*</span></label>
        <select><option>Instalação de tomadas</option><option>Troca de disjuntor</option></select>
        <span class="ajuda">Valor de referência R$ 187,50, prazo padrão de 3 dias.</span>
      </div>
      <div class="campo estreito">
        <label>Prioridade</label>
        <select><option>Normal</option><option>Baixa</option><option>Alta</option><option>Urgente</option></select>
      </div>
    </div>

    <div class="campo largo com-erro">
      <label>Descrição do problema <span class="obrigatorio">*</span></label>
      <textarea>tomada queimada</textarea>
      <span class="erro">Descreva com mais detalhe: são necessários pelo menos 20 caracteres.</span>
      <span class="ajuda">Quanto mais claro o pedido, menor a chance de o prestador chegar sem o material certo.</span>
    </div>

    <div class="linha">
      <div class="campo">
        <label>Prazo desejado</label>
        <input type="text" value="25/09/2026">
        <span class="ajuda">Se ficar em branco, o sistema aplica o prazo padrão do serviço e mostra a data calculada.</span>
      </div>
      <div class="campo">
        <label>Local do atendimento</label>
        <input type="text" value="Rua Néo Alves Martins, 2810 - Zona 3">
      </div>
    </div>
  </div>
  <div class="rodape-form">
    <a class="btn btn-neutro" href="T16-minhas-solicitacoes.html">Cancelar</a>
    <a class="btn btn-primario" href="T16-minhas-solicitacoes.html">Enviar solicitação</a>
  </div>
</div>"""

# ---------------------------------------------------------------- T18

ORDEM_CLIENTE = """<div class="aviso ok">
  <div>
    <strong>Serviço concluído em 15/09/2026, dentro do prazo.</strong>
    A avaliação fica disponível agora e pode ser lançada uma única vez (RN08).
  </div>
</div>

<div class="colunas">
  <div class="cartao">
    <h2>Acompanhamento</h2>
    <div class="cartao-corpo">
      <div class="trilha">
        <span class="passo feito">Aberta</span>  <span class="passo feito">Atribuída</span>  <span class="passo feito">Em execução</span>  <span class="passo atual">Concluída</span>
      </div>
      <ul class="tempo" style="margin-top:16px">
        <li>
          <strong>Serviço concluído</strong>
          <span class="quando">15/09/2026 às 16:20</span>
          troquei o disjuntor geral por um de 40A, testei com a camara ligada e identifiquei o quadro com etiqueta nova
        </li>
        <li><strong>Execução iniciada</strong><span class="quando">15/09/2026 às 09:10</span></li>
        <li><strong>Atribuída a Elétrica Santos</strong><span class="quando">12/09/2026 às 14:05</span></li>
        <li><strong>Solicitação enviada</strong><span class="quando">12/09/2026 às 11:32</span></li>
      </ul>
    </div>
  </div>

  <div class="cartao" style="flex:0 1 400px">
    <h2>Avaliar o atendimento</h2>
    <div class="cartao-corpo">
      <div class="campo largo">
        <label>Nota <span class="obrigatorio">*</span></label>
        <div class="notas-avaliacao">
          <a class="nota-opcao" href="T18-ordem-cliente.html">1</a>
          <a class="nota-opcao" href="T18-ordem-cliente.html">2</a>
          <a class="nota-opcao" href="T18-ordem-cliente.html">3</a>
          <a class="nota-opcao" href="T18-ordem-cliente.html">4</a>
          <a class="nota-opcao escolhida" href="T18-ordem-cliente.html">5</a>
        </div>
        <span class="ajuda">1 para muito ruim, 5 para muito bom.</span>
      </div>
      <div class="campo largo">
        <label>Comentário</label>
        <textarea placeholder="Conte como foi o atendimento (opcional)">chegou no horario e deixou tudo limpo. so demorou um pouco pra achar o quadro</textarea>
      </div>
    </div>
    <div class="rodape-form">
      <a class="btn btn-primario" href="T16-minhas-solicitacoes.html">Enviar avaliação</a>
    </div>
  </div>
</div>"""

# --------------------------------------------------------------- mapa

MAPA = """<div class="mapa">
  <h1>Protótipo do SGP</h1>
  <p class="intro">Sistema de gestão de prestadores, equipe 8. São as 18 telas do MVP, navegáveis entre si.
  Os dados são fictícios e a data de referência é 22/09/2026.</p>

  <div class="grupo">
    <h2>Acesso</h2>
    <div class="telas">
      <a href="T01-login.html"><strong>Login</strong><span>T01, entrada por e-mail e senha</span></a>
    </div>
  </div>

  <div class="grupo">
    <h2>Administrador</h2>
    <div class="telas">
      <a href="T02-painel-administrador.html"><strong>Painel do dia</strong><span>T02, vencimentos e ordens que precisam de ação</span></a>
      <a href="T11-ordens.html"><strong>Ordens de serviço</strong><span>T11, lista com filtro por situação</span></a>
      <a href="T12-ordem-administrador.html"><strong>Ordem aberta</strong><span>T12, dados, situação e histórico</span></a>
      <a href="T12b-atribuir-ordem.html"><strong>Atribuir prestador</strong><span>T12, aptos e o motivo de cada inapto</span></a>
      <a href="T12c-cancelar-ordem.html"><strong>Cancelar ordem</strong><span>T12, motivo obrigatório</span></a>
      <a href="T10-vencimentos.html"><strong>Vencimentos</strong><span>T10, vencidos e a vencer em 30 dias</span></a>
      <a href="T03-prestadores.html"><strong>Prestadores</strong><span>T03, lista com filtro por situação e categoria</span></a>
      <a href="T04-prestador-dados.html"><strong>Ficha do prestador</strong><span>T04, dados cadastrais</span></a>
      <a href="T04b-prestador-categorias.html"><strong>Categorias do prestador</strong><span>T04, habilitação por categoria</span></a>
      <a href="T04c-prestador-documentos.html"><strong>Documentos do prestador</strong><span>T04, validade e versões anteriores</span></a>
      <a href="T04d-prestador-situacao.html"><strong>Situação cadastral</strong><span>T04, alteração com motivo e histórico</span></a>
      <a href="T05-clientes.html"><strong>Clientes</strong><span>T05, lista de clientes</span></a>
      <a href="T06-cliente-cadastro.html"><strong>Ficha do cliente</strong><span>T06, dados e endereço</span></a>
      <a href="T08-servicos.html"><strong>Serviços</strong><span>T08, catálogo com valor e prazo padrão</span></a>
      <a href="T09-servico-cadastro.html"><strong>Ficha do serviço</strong><span>T09, dados do serviço</span></a>
      <a href="T07-categorias.html"><strong>Categorias</strong><span>T07, lista e inclusão</span></a>
    </div>
  </div>

  <div class="grupo">
    <h2>Prestador</h2>
    <div class="telas">
      <a href="T13-minhas-ordens.html"><strong>Minhas ordens</strong><span>T13, apenas as ordens do prestador logado</span></a>
      <a href="T14-ordem-execucao.html"><strong>Execução da ordem</strong><span>T14, andamento e conclusão com relato</span></a>
      <a href="T15-meus-documentos.html"><strong>Meus documentos</strong><span>T15, envio com validação de formato</span></a>
    </div>
  </div>

  <div class="grupo">
    <h2>Cliente</h2>
    <div class="telas">
      <a href="T16-minhas-solicitacoes.html"><strong>Minhas solicitações</strong><span>T16, acompanhamento das próprias ordens</span></a>
      <a href="T17-nova-solicitacao.html"><strong>Nova solicitação</strong><span>T17, abertura do pedido</span></a>
      <a href="T18-ordem-cliente.html"><strong>Acompanhar e avaliar</strong><span>T18, nota de 1 a 5 e comentário</span></a>
    </div>
  </div>
</div>"""

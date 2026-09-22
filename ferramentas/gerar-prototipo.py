# -*- coding: utf-8 -*-
"""
gera as telas do prototipo navegavel do sgp na pasta prototipos/.

cada tela é um arquivo html estatico, sem javascript e sem dependencia externa,
pra abrir com dois cliques e funcionar tambem na apresentacao sem internet. o
cabecalho, o menu lateral e o rodape sao montados aqui, entao cada tela precisa
declarar apenas o proprio conteudo.

uso:
    python ferramentas/gerar-prototipo.py
"""

import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(RAIZ, "prototipos")

# ---------------------------------------------------------------- menus

MENUS = {
    "administrador": [
        ("T02-painel-administrador.html", "Painel"),
        ("T11-ordens.html", "Ordens de serviço"),
        ("T03-prestadores.html", "Prestadores"),
        ("T10-vencimentos.html", "Vencimentos"),
        ("T05-clientes.html", "Clientes"),
        ("T08-servicos.html", "Catálogo de serviços"),
        ("T07-categorias.html", "Categorias"),
    ],
    "prestador": [
        ("T13-minhas-ordens.html", "Minhas ordens"),
        ("T15-meus-documentos.html", "Meus documentos"),
    ],
    "cliente": [
        ("T16-minhas-solicitacoes.html", "Minhas solicitações"),
        ("T17-nova-solicitacao.html", "Nova solicitação"),
    ],
    "": [],
}

USUARIO = {
    "administrador": ("Marina Prado", "Administradora"),
    "prestador": ("Elétrica Boratto ME", "Prestador"),
    "cliente": ("Supermercado Ponto Certo", "Cliente"),
    "": ("", ""),
}

PAGINA = """<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{codigo} · {titulo} · SGP</title>
<link rel="stylesheet" href="estilo.css">
</head>
<body class="{classe_body}">
{corpo}
</body>
</html>
"""

CASCA = """<header class="topo">
  <a class="marca" href="index.html">SGP<span>sistema de gestão de prestadores</span></a>
  <div class="usuario">
    <div class="usuario-dados">
      <strong>{usuario}</strong>
      <span>{papel}</span>
    </div>
    <a class="btn btn-neutro btn-pequeno" href="T01-login.html">Sair</a>
  </div>
</header>
<div class="corpo">
  <nav class="menu">
    {itens_menu}
    <a class="menu-item menu-mapa" href="index.html">Mapa do protótipo</a>
  </nav>
  <main class="conteudo">
    <div class="cabecalho-tela">
      <div>
        <span class="codigo-tela">{codigo}</span>
        <h1>{titulo}</h1>
        {subtitulo}
      </div>
      {acoes}
    </div>
    {conteudo}
    {notas}
  </main>
</div>
"""


def menu(perfil, ativo):
    itens = []
    for arquivo, rotulo in MENUS[perfil]:
        classe = "menu-item ativo" if arquivo == ativo else "menu-item"
        itens.append('<a class="%s" href="%s">%s</a>' % (classe, arquivo, rotulo))
    return "\n    ".join(itens)


def notas(itens):
    if not itens:
        return ""
    linhas = "".join("<li>%s</li>" % i for i in itens)
    return ('<section class="notas">'
            '<h2>Estados e validações previstos nesta tela</h2>'
            '<ul>%s</ul></section>' % linhas)


def tela(arquivo, codigo, titulo, perfil, conteudo, subtitulo="", acoes="", obs=()):
    corpo = CASCA.format(
        usuario=USUARIO[perfil][0],
        papel=USUARIO[perfil][1],
        itens_menu=menu(perfil, arquivo),
        codigo=codigo,
        titulo=titulo,
        subtitulo='<p class="subtitulo">%s</p>' % subtitulo if subtitulo else "",
        acoes='<div class="acoes-tela">%s</div>' % acoes if acoes else "",
        conteudo=conteudo,
        notas=notas(obs),
    )
    html = PAGINA.format(codigo=codigo, titulo=titulo, classe_body="app", corpo=corpo)
    destino = os.path.join(SAIDA, arquivo)
    open(destino, "w", encoding="utf-8").write(html)
    print("  gerado:", arquivo)


def solta(arquivo, codigo, titulo, corpo):
    """telas sem menu lateral, como o login e o mapa do prototipo."""
    html = PAGINA.format(codigo=codigo, titulo=titulo, classe_body="centro", corpo=corpo)
    open(os.path.join(SAIDA, arquivo), "w", encoding="utf-8").write(html)
    print("  gerado:", arquivo)


if __name__ == "__main__":
    import telas_prototipo as T

    if not os.path.isdir(SAIDA):
        os.makedirs(SAIDA)

    print("gerando o prototipo em prototipos/")

    solta("index.html", "mapa", "Mapa do protótipo", T.MAPA)
    solta("T01-login.html", "T01", "Entrar no sistema", T.LOGIN)

    # ---------------------------------------------------------- administrador
    tela("T02-painel-administrador.html", "T02", "Painel do administrador", "administrador", T.PAINEL_ADM,
         subtitulo="Segunda-feira, 22 de setembro de 2026",
         obs=("Cada indicador leva para a listagem correspondente ja filtrada.",
              "Quando nao houver pendencia, o cartao mostra a mensagem de tudo em dia no lugar da tabela vazia."))

    tela("T03-prestadores.html", "T03", "Prestadores", "administrador", T.PRESTADORES,
         subtitulo="Cadastro da rede de terceirizados",
         acoes='<a class="btn btn-primario" href="T04-prestador-dados.html">Novo prestador</a>',
         obs=("A listagem é paginada e responde em ate 3 segundos com 5 mil registros (RNF06).",
              "Busca sem resultado mostra a mensagem de nenhum registro encontrado, nao uma tabela vazia.",
              "Prestador com ordem atribuida ou em execucao nao pode ser inativado (RN11)."))

    tela("T04-prestador-dados.html", "T04", "Elétrica Boratto ME", "administrador", T.PRESTADOR_DADOS,
         subtitulo="Cadastro do prestador",
         obs=("O CNPJ é validado pelo digito verificador e nao pode se repetir entre cadastros ativos (RN10).",
              "Enquanto houver erro de validacao o formulario nao é enviado e o campo fica destacado.",
              "Toda gravacao devolve mensagem de confirmacao ou de erro (RNF05)."))

    tela("T04b-prestador-categorias.html", "T04", "Elétrica Boratto ME", "administrador", T.PRESTADOR_CATEGORIAS,
         subtitulo="Categorias em que o prestador atua",
         obs=("Desmarcar uma categoria com ordem em andamento é recusado, informando quais ordens impedem.",
              "A habilitacao é o que faz o prestador aparecer na atribuicao daquela categoria (RN04)."))

    tela("T04c-prestador-documentos.html", "T04", "Elétrica Boratto ME", "administrador", T.PRESTADOR_DOCUMENTOS,
         subtitulo="Documentação do prestador",
         acoes='<a class="btn btn-primario" href="T04c-prestador-documentos.html">Enviar documento</a>',
         obs=("Documento renovado entra como versao atual e a anterior fica no historico, nunca é apagada.",
              "Vencimento de documento obrigatorio muda a situacao para pendente automaticamente (RN02)."))

    tela("T04d-prestador-situacao.html", "T04", "Elétrica Boratto ME", "administrador", T.PRESTADOR_SITUACAO,
         subtitulo="Situação cadastral e histórico",
         obs=("O motivo exige no minimo 10 caracteres.",
              "A alteracao vai para o historico e para o log de auditoria (RF19).",
              "Quando a mudanca é automatica pela RN02, o responsavel registrado é o proprio sistema."))

    tela("T05-clientes.html", "T05", "Clientes", "administrador", T.CLIENTES,
         subtitulo="Quem pode solicitar serviço",
         acoes='<a class="btn btn-primario" href="T06-cliente-cadastro.html">Novo cliente</a>',
         obs=("Cliente inativo nao aparece na abertura de novas ordens, mas continua no historico.",))

    tela("T06-cliente-cadastro.html", "T06", "Supermercado Ponto Certo", "administrador", T.CLIENTE_CADASTRO,
         subtitulo="Cadastro do cliente",
         obs=("CPF e CNPJ sao unicos entre os cadastros ativos (RN10).",))

    tela("T07-categorias.html", "T07", "Categorias de serviço", "administrador", T.CATEGORIAS,
         subtitulo="Classificação usada por serviços e prestadores",
         obs=("Categoria inativa some das listas de selecao, mas continua valendo para os registros antigos.",
              "O nome da categoria nao pode se repetir."))

    tela("T08-servicos.html", "T08", "Catálogo de serviços", "administrador", T.SERVICOS,
         subtitulo="O que pode ser solicitado",
         acoes='<a class="btn btn-primario" href="T09-servico-cadastro.html">Novo serviço</a>',
         obs=("O prazo padrao do servico é usado quando o cliente nao informa prazo na solicitacao.",))

    tela("T09-servico-cadastro.html", "T09", "Instalação de tomadas", "administrador", T.SERVICO_CADASTRO,
         subtitulo="Cadastro do serviço",
         obs=("O valor de referencia aceita apenas numero positivo.",))

    tela("T10-vencimentos.html", "T10", "Painel de vencimentos", "administrador", T.VENCIMENTOS,
         subtitulo="Documentos vencidos e os que vencem nos próximos 30 dias",
         obs=("Sem nenhum vencimento no periodo, a tela mostra a mensagem informando isso, e nao uma tabela vazia.",
              "A situacao do prestador pode ser alterada direto daqui, sem abrir o cadastro (UC09 estende UC11)."))

    tela("T11-ordens.html", "T11", "Ordens de serviço", "administrador", T.ORDENS,
         subtitulo="Todas as ordens da empresa",
         obs=("O administrador é o unico perfil que ve as ordens de todos os clientes e prestadores.",
              "Ordem cancelada continua na lista, com o motivo registrado, e nunca é excluida."))

    tela("T12-ordem-administrador.html", "T12", "Ordem OS-2026-0147", "administrador", T.ORDEM_ADM,
         subtitulo="Visão do administrador",
         obs=("As acões disponiveis mudam conforme o status: ordem concluida nao pode ser cancelada nem editada (RN06).",
              "Trocar o prestador reabre a verificacao de aptidao (UC22)."))

    tela("T12b-atribuir-ordem.html", "T12", "Atribuir prestador", "administrador", T.ATRIBUIR,
         subtitulo="Ordem OS-2026-0147 · Desentupimento de pia",
         obs=("A aptidao é verificada de novo no servidor no momento da confirmacao (RNF02).",
              "Se o prestador ficar inapto entre a abertura da tela e a confirmacao, a atribuicao é recusada e a lista recarregada.",
              "Sem nenhum prestador apto, a tela informa e oferece o caminho para habilitar ou regularizar alguem."))

    tela("T12c-cancelar-ordem.html", "T12", "Cancelar ordem", "administrador", T.CANCELAR,
         subtitulo="Ordem OS-2026-0147",
         obs=("O botao de confirmar so libera quando o motivo atinge 10 caracteres (RN07).",
              "O cancelamento é registrado no log com usuario, data e hora (RF19)."))

    # ------------------------------------------------------------- prestador
    tela("T13-minhas-ordens.html", "T13", "Minhas ordens", "prestador", T.MINHAS_ORDENS,
         subtitulo="Somente as ordens atribuídas a você",
         obs=("O recorte por prestador é feito no servidor. Uma requisicao montada por fora é recusada (RNF02).",
              "Sem nenhuma ordem atribuida, a lista mostra a mensagem de que nao ha ordem no momento."))

    tela("T14-ordem-execucao.html", "T14", "Ordem OS-2026-0148", "prestador", T.ORDEM_EXECUCAO,
         subtitulo="Instalação de tomadas · Supermercado Ponto Certo",
         obs=("A conclusao exige o relato do que foi executado (fluxo de excecao E4.1).",
              "Ao concluir, o sistema compara a data com o prazo e marca a ordem como no prazo ou em atraso (RN12).",
              "Depois de concluida, a ordem fica bloqueada para edicao (RN06)."))

    tela("T15-meus-documentos.html", "T15", "Meus documentos", "prestador", T.MEUS_DOCUMENTOS,
         subtitulo="Mantenha a documentação em dia para continuar recebendo ordens",
         obs=("Sao aceitos apenas PDF, JPG e PNG, com ate 10 MB por arquivo (RNF09).",
              "Data de emissao posterior a validade é recusada, com os dois campos destacados.",
              "O envio da versao renovada mantem a anterior no historico."))

    # --------------------------------------------------------------- cliente
    tela("T16-minhas-solicitacoes.html", "T16", "Minhas solicitações", "cliente", T.MINHAS_SOLICITACOES,
         subtitulo="Acompanhe o que você pediu",
         acoes='<a class="btn btn-primario" href="T17-nova-solicitacao.html">Nova solicitação</a>',
         obs=("O cliente ve apenas as proprias ordens e nao tem acesso a lista de prestadores (RNF02).",
              "A acao avaliar so aparece depois que a ordem é concluida (RN08)."))

    tela("T17-nova-solicitacao.html", "T17", "Nova solicitação", "cliente", T.NOVA_SOLICITACAO,
         subtitulo="Descreva o serviço que você precisa",
         obs=("A descricao exige no minimo 20 caracteres.",
              "Prazo anterior a hoje é recusado. Sem prazo informado, o sistema aplica o prazo padrao do servico.",
              "A ordem nasce com status aberta e recebe um numero visivel ao cliente."))

    tela("T18-ordem-cliente.html", "T18", "Ordem OS-2026-0144", "cliente", T.ORDEM_CLIENTE,
         subtitulo="Troca de disjuntor · concluída em 15/09/2026",
         obs=("A avaliacao so pode ser lancada uma vez, e apenas pelo cliente titular da ordem (RN08).",
              "Depois de enviada, ela aparece em modo somente leitura.",
              "A nota entra no calculo da media do prestador dos ultimos 12 meses (RN09)."))

    print("pronto. abra prototipos/index.html para navegar.")

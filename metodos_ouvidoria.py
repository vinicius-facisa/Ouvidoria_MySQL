from operacoesbd import *

def listar_todas_manifestacoes(conexao):
    """Lista todas as manifestações cadastradas"""
    consulta = 'select * from manifestacao'
    manifestacoes = listarBancoDados(conexao, consulta)

    if len(manifestacoes) == 0:
        print("Não existem manifestações cadastradas")
    else:
        print("Lista de Manifestações:")
        for item in manifestacoes:
            print(f"- Código: {item[0]} | Tipo: {item[1]} | Título: {item[2]} | Nome: {item[4]}")

def listar_manifestacoes_por_tipo(conexao):
    """Lista manifestações por tipo específico"""
    tipo = input("Digite o tipo (reclamação, elogio, sugestão): ").lower()
    consulta = 'select * from manifestacao where tipo = %s'
    dados = [tipo]

    manifestacoes = listarBancoDados(conexao, consulta, dados)

    if len(manifestacoes) == 0:
        print(f"Não existem manifestações do tipo '{tipo}' cadastradas")
    else:
        print(f"Lista de Manifestações - Tipo: {tipo}")
        for item in manifestacoes:
            print(f"- Código: {item[0]} | Título: {item[2]} | Descrição: {item[3]} | Nome: {item[4]}")

def criar_nova_manifestacao(conexao):
    """Cria uma nova manifestação"""
    titulo = input("Digite o título da manifestação: ")
    descricao = input("Digite a descrição da manifestação: ")
    tipo = input("Digite o tipo (reclamação, elogio, sugestão): ").lower()
    nome = input("Digite seu nome: ")

    consulta = 'insert into manifestacao (tipo, titulo, descricao, nome) values(%s,%s,%s,%s)'
    dados = [tipo, titulo, descricao, nome]

    codigoManifestacao = insertNoBancoDados(conexao, consulta, dados)
    if codigoManifestacao:
        print(f"Nova manifestação criada com sucesso! Código: {codigoManifestacao}")
    else:
        print("Erro ao criar manifestação.")

def exibir_quantidade_manifestacoes(conexao):
    """Exibe a quantidade total de manifestações"""
    consulta = 'select count(*) from manifestacao'
    quantidade = listarBancoDados(conexao, consulta)
    print(f"Quantidade de manifestações: {quantidade[0][0]}")

def pesquisar_manifestacao_por_codigo(conexao):
    """Pesquisa uma manifestação por código"""
    try:
        codigo = int(input("Digite o código da manifestação: "))
        consulta = 'select * from manifestacao where codigo = %s'
        dados = [codigo]

        manifestacoes = listarBancoDados(conexao, consulta, dados)

        if len(manifestacoes) == 0:
            print("Não existe manifestação para o código informado")
        else:
            print("Manifestação Encontrada:")
            item = manifestacoes[0]
            print(f"Código: {item[0]}")
            print(f"Tipo: {item[1]}")
            print(f"Título: {item[2]}")
            print(f"Descrição: {item[3]}")
            print(f"Nome: {item[4]}")
    except:
        print("Por favor, digite apenas números.")

def excluir_manifestacao_por_codigo(conexao):
    """Exclui uma manifestação por código"""
    try:
        codigo = int(input("Digite o código da manifestação a ser removida: "))
        consulta = 'delete from manifestacao where codigo = %s'
        dados = [codigo]

        linhasAfetadas = excluirBancoDados(conexao, consulta, dados)

        if linhasAfetadas == 0:
            print("Não existe manifestação para o código informado.")
        else:
            print("Manifestação removida com sucesso!")
    except:
        print("Por favor, digite apenas números.")
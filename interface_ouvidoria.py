from operacoesbd import *
from metodos_ouvidoria import *

def main():
    conexao = criarConexao('127.0.0.1','root','12345','ouvidoria')
    opcao = 1

    while opcao != 7:
        print("\n===== SISTEMA DE OUVIDORIA =====")
        print("1) Listagem das Manifestações")
        print("2) Listagem de Manifestações por Tipo")
        print("3) Criar uma nova Manifestação")
        print("4) Exibir quantidade de manifestações")
        print("5) Pesquisar uma manifestação por código")
        print("6) Excluir uma Manifestação pelo Código")
        print("7) Sair do Sistema")
        
        try:
            opcao = int(input("Digite a sua opção: "))
        except:
            print("Por favor, digite apenas números de 1 a 7.")
            continue

        if opcao == 1:
            listar_todas_manifestacoes(conexao)
        elif opcao == 2:
            listar_manifestacoes_por_tipo(conexao)
        elif opcao == 3:
            criar_nova_manifestacao(conexao)
        elif opcao == 4:
            exibir_quantidade_manifestacoes(conexao)
        elif opcao == 5:
            pesquisar_manifestacao_por_codigo(conexao)
        elif opcao == 6:
            excluir_manifestacao_por_codigo(conexao)
        elif opcao != 7:
            print("Opção inválida")

    encerrarConexao(conexao)
    print("Obrigado por usar o Sistema de Ouvidoria!")

if __name__ == "__main__":
    main()
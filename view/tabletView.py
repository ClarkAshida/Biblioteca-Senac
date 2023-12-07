from controller.tabletController import AdicionarTablet, ListarTablet, BuscarTablet, ApagarTablet, AtualizarTablet
from datetime import datetime

class TabletView:
    @staticmethod
    def cadastrar():
        try:
            nome = input("Digite o nome do tablet: ")
            data = datetime.now()
            marca = input("Digite a marca do tablet: ")
            codigo_modelo = int(input("Digite o código do modelo do tablet: "))

            try:
                AdicionarTablet.post(nome, data, marca, codigo_modelo)
            except Exception as e:
                print(f"Erro ao cadastrar tablet: {e}")

        except ValueError:
            print("Erro: Código do modelo do tablet inválido. Certifique-se de inserir um número inteiro.")

    @staticmethod
    def listar():
        try:
            return ListarTablet.get()
        except Exception as e:
            print(f"Erro ao listar tablets: {e}")

    @staticmethod
    def buscar_por_id():
        try:
            id = int(input("Digite o ID do tablet que deseja buscar: "))
            tablet = BuscarTablet.get(id)
            print(tablet)
        except ValueError:
            print("Erro: ID do tablet inválido. Certifique-se de inserir um número inteiro.")

    @staticmethod
    def excluir():
        try:
            id = int(input("Digite o ID do tablet que deseja excluir: "))
            ApagarTablet.get(id)
        except ValueError:
            print("Erro: ID do tablet inválido. Certifique-se de inserir um número inteiro.")

    @staticmethod
    def atualizar():
        try:
            id = int(input("Digite o ID do tablet que deseja atualizar: "))
            nome = input("Digite o novo nome do tablet: ")
            data = datetime.now()
            marca = input("Digite a nova marca do tablet: ")
            codigo_modelo = int(input("Digite o novo código do modelo do tablet: "))
            status = int(input("Digite o novo status do tablet: "))

            # Adiciona exceção se houver um problema durante a atualização do tablet
            try:
                AtualizarTablet.get(id, nome, data, marca, codigo_modelo, status)
                print("Tablet atualizado com sucesso!")
            except Exception as e:
                print(f"Erro ao atualizar tablet: {e}")

        except ValueError:
            print("Erro: Código do modelo do tablet ou status inválido. Certifique-se de inserir números inteiros.")


    def menu():
        while True:
            print("\nBem-vindo ao Gerenciador da Biblioteca SENAC!"
                  "\nInsira a opção desejada:"
                  "\n1- Cadastrar Tablet"
                  "\n2- Listar Tablets"
                  "\n3- Buscar Tablet por ID"
                  "\n4- Remover Tablet"
                  "\n5- Atualizar Status do Tablet"
                  "\n6- Voltar")

            op = int(input())

            if op == 1:
                TabletView.cadastrar()
            elif op == 2:
                TabletView.listar()
            elif op == 3:
                TabletView.buscar_por_id()
            elif op == 4:
                TabletView.excluir()
            elif op == 5:
                TabletView.atualizar()
            elif op == 6:
                break
            elif op < 1 or op > 6:
                print("Opção inválida. Insira uma válida.")
                break
            else:
                print("Opção inválida. Insira uma válida.")
                break

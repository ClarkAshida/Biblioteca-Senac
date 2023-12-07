from controller.registroDeEmprestimoController import AdicionarRegistroLivro, AdicionarRegistroTablet, AtualizarRegistro, ApagarRegistro, ListarRegistro, BuscarRegistroPorID, Multa
from datetime import datetime, timedelta


class RegistroDeEmprestimoView:
    def cadastrar_livro():
        try:
            codigo_usuario = int(input("Digite o código do usuário: "))
            codigo_livro = int(input("Digite o código do livro: "))
            data_inicio = datetime.now()
            data_final = data_inicio + timedelta(7)

            # Adiciona exceção se houver um problema durante a inserção do registro
            try:
                AdicionarRegistroLivro.post(codigo_usuario, codigo_livro, data_inicio, data_final)
            except Exception as e:
                print(f"Erro ao cadastrar livro: {e}")

        except ValueError:
            print("Erro: Código do usuário ou do livro inválido. Certifique-se de inserir um número inteiro.")

    def cadastrar_tablet():
        try:
            codigo_usuario = int(input("Digite o código do usuário: "))
            codigo_tablet = int(input("Digite o código do tablet: "))
            data_inicio = datetime.now()
            data_final = data_inicio + timedelta(7)

            try:
                AdicionarRegistroTablet.post(codigo_usuario, codigo_tablet, data_inicio, data_final)
            except Exception as e:
                print(f"Erro ao cadastrar tablet: {e}")
        except ValueError:
            print("Erro: Código do usuário ou do tablet inválido. Certifique-se de inserir um número inteiro.")

    def listar():
        try:
            ListarRegistro.get()
        except Exception as e:
            print(f"Erro ao listar registros: {e}")

    def buscar_por_id():
        try:
            id_registro = int(input("Digite o ID do registro que deseja buscar: "))
            BuscarRegistroPorID.get(id_registro)
        except ValueError:
            print("Erro: ID do registro inválido. Certifique-se de inserir um número inteiro.")

    def atualizar_status():
        try:
            id_registro = int(input("Digite o ID do registro que deseja atualizar: "))
            novo_status = int(input("Digite o novo status do registro: "))
            AtualizarRegistro.get(id_registro, novo_status)
        except ValueError:
            print("Erro: ID do registro ou novo status inválido. Certifique-se de inserir números inteiros.")

    def excluir():
        try:
            id_registro = int(input("Digite o ID do registro que deseja excluir: "))
            ApagarRegistro.get(id_registro)
        except ValueError:
            print("Erro: ID do registro inválido. Certifique-se de inserir um número inteiro.")

    def menu():
        while True:
            print("\nBem-vindo ao Gerenciador de Empréstimos da Biblioteca SENAC!"
                  "\nInsira a opção desejada:"
                  "\n1- Cadastrar Empréstimo de Livro"
                  "\n2- Cadastrar Empréstimo de Tablet"
                  "\n3- Listar Empréstimos"
                  "\n4- Buscar Empréstimo por ID"
                  "\n5- Atualizar Status de Empréstimo"
                  "\n6- Excluir Empréstimo"
                  "\n7- Voltar")

            op = int(input())

            if op == 1:
                RegistroDeEmprestimoView.cadastrar_livro()
            elif op == 2:
                RegistroDeEmprestimoView.cadastrar_tablet()
            elif op == 3:
                RegistroDeEmprestimoView.listar()
            elif op == 4:
                RegistroDeEmprestimoView.buscar_por_id()
            elif op == 5:
                RegistroDeEmprestimoView.atualizar_status()
            elif op == 6:
                RegistroDeEmprestimoView.excluir()
            elif op == 7:
                break
            elif op < 1 or op > 7:
                print("Opção inválida. Insira uma válida.")
                break
            else:
                print("Opção inválida. Insira uma válida.")
                break

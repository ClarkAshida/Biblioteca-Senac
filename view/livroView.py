from controller.livroController import AdicionarLivroController, ListarLivrosController, BuscarLivroController, ApagarLivroController, AtualizarLivroController
from datetime import datetime

class LivroView:
    @staticmethod
    def cadastrar():
        try:
            nome = input("Digite o nome do livro: ")
            data = datetime.now()
            codigo_titulo = int(input("Digite o código do título do livro: "))
            autor = input("Digite o autor do livro: ")
            editora = input("Digite a editora do livro: ")

            # Adiciona exceção se houver um problema durante o cadastro do livro
            try:
                return AdicionarLivroController.post(nome, data, codigo_titulo, autor, editora)
            except Exception as e:
                print(f"Erro ao cadastrar livro: {e}")

        except ValueError:
            print("Erro: Código do título do livro inválido. Certifique-se de inserir um número inteiro.")

    @staticmethod
    def listar():
        try:
            return ListarLivrosController.get()
        except Exception as e:
            print(f"Erro ao listar livros: {e}")

    @staticmethod
    def buscar_por_id():
        try:
            id = int(input("Digite o ID do livro que deseja buscar: "))
            return BuscarLivroController.get(id)
        except ValueError:
            print("Erro: ID do livro inválido. Certifique-se de inserir um número inteiro.")
        except IndexError:
            print("Erro: ID inválido. Certifique-se de inserior um número inteiro.")

    @staticmethod
    def excluir():
        try:
            id = int(input("Digite o ID do livro que deseja excluir: "))
            return ApagarLivroController.get(id)
        except ValueError:
            print("Erro: ID do livro inválido. Certifique-se de inserir um número inteiro.")

    @staticmethod
    def atualizar():
        try:
            id = int(input("Digite o ID do livro que deseja atualizar: "))
            nome = input("Digite o novo nome do livro: ")
            data = datetime.now()
            codigo_titulo = int(input("Digite o novo código do título do livro: "))
            autor = input("Digite o novo autor do livro: ")
            editora = input("Digite a nova editora do livro: ")
            status = int(input("Digite o novo status do livro: "))

            # Adiciona exceção se houver um problema durante a atualização do livro
            try:
                AtualizarLivroController.get(id, nome, data, codigo_titulo, autor, editora, status)
                print("Livro atualizado com sucesso!")
            except Exception as e:
                print(f"Erro ao atualizar livro: {e}")

        except ValueError:
            print("Erro: Código do título do livro ou status inválido. Certifique-se de inserir números inteiros.")

    def menu():
        while True:
            print("\nBem-vindo ao Gerenciador da Biblioteca SENAC!"
                  "\nInsira a opção desejada:"
                  "\n1- Cadastrar Livro"
                  "\n2- Listar Livros"
                  "\n3- Buscar Livro por ID"
                  "\n4- Remover Livro"
                  "\n5- Atualizar Status do Livro"
                  "\n6- Voltar")

            op = int(input())

            if op == 1:
                LivroView.cadastrar()
            elif op == 2:
                LivroView.listar()
            elif op == 3:
                LivroView.buscar_por_id()
            elif op == 4:
                LivroView.excluir()
            elif op == 5:
                LivroView.atualizar()
            elif op == 6:
                break
            elif op < 1 or op > 6:
                print("Opção inválida. Insira uma válida.")
                break
            else:
                print("Opção inválida. Insira uma válida.")
                break

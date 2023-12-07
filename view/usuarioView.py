from controller.usuarioController import AdicionarUsuario, ListarUsuario, BuscarUsuario, ApagarUsuario, AtualizarUsuario

class UsuarioView:
    @staticmethod
    def cadastro():
        try:
            nome = input("Digite o nome do usuário: ")
            idade = int(input("Digite a idade do usuário: "))
            tipoDeUsuario = int(input("Escolha o tipo de Usuário (1 para Aluno e 2 para Professor): "))
            
            if tipoDeUsuario in {1, 2}:
                return AdicionarUsuario.post(nome, idade, tipoDeUsuario)
            else:
                raise ValueError("Escolha um tipo de Usuário válido (1 para Aluno e 2 para Professor).")

        except ValueError as ve:
            print(f"Erro ao cadastrar usuário: {ve}")
            return None  # Ou outra forma de lidar com o erro, se necessário.

    @staticmethod
    def listar():
        try:
            return ListarUsuario.get()
        except Exception as e:
            print(f"Erro ao listar usuários: {e}")
            return None

    @staticmethod
    def buscar(id):
        try:
            return BuscarUsuario.get(id)
        except IndexError:
            print("Erro: ID de usuário não encontrado.")
            return None

    @staticmethod
    def excluir(id):
        try:
            return ApagarUsuario.get(id)
        except IndexError:
            print("Erro: ID de usuário não encontrado.")
            return None

    @staticmethod
    def atualizar(id):
        try:
            return AtualizarUsuario.get(id)
        except IndexError:
            print("Erro: ID de usuário não encontrado.")
            return None


    def menu():
        while True:
            print(f"\nBem-vindo ao Gerenciador da Biblitoca SENAC!"
            "\nInsira a opção desejada:"
            "\n1- Cadastrar Usuário"
            "\n2- Listar Usuários"
            "\n3- Buscar Usuário por ID"
            "\n4- Remover Usuário"
            "\n5- Devolver Livro"
            "\n6- Voltar")
            op = int(input())

            if op == 1:
                UsuarioView.cadastro()
            elif op == 2:
                UsuarioView.listar()
            elif op == 3:
                id=int(input("Insira o ID que procura: "))
                UsuarioView.buscar(id)
            elif op == 4:
                print("ATENÇÃO\nESSA AÇÃO É DE CARÁTER CRÍTICO!")
                id= int(input("Insira o Id do usuário a ser removido: "))
                UsuarioView.excluir(id)
            elif op == 5:
                print("ATENÇÃO\nESSA OPÇÃO SINALIZA A DEVOLUÇÃO DE UM LIVRO POR PARTE DE UM ALUNO!")
                id= int(input("Insira o seu Id: "))
                UsuarioView.atualizar(id)
            elif op == 6:
                break
            elif op < 1 or op > 6:
                print("opção inválida. Insira uma válida")
                break
            else:
                print("opção inválida. Insira uma válida")
                break

        

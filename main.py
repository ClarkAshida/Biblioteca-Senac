from view.usuarioView import UsuarioView
from view.livroView import LivroView
from view.tabletView import TabletView
from view.registroDeEmprestimoView import RegistroDeEmprestimoView

if __name__=='__main__':
    while True:
        print(f"\nBem-vindo ao Gerenciador da Biblioteca SENAC!"
        "\nInsira a opção desejada: "
        "\n1- Gerenciar usuários"
        "\n2- Gerenciar livros"
        "\n3- Gerenciar tablets"
        "\n4- Gerenciar registros de empréstimo")

        option = int(input("Opção: "))
        if option == 1:
            UsuarioView.menu()
        elif option == 2:
            LivroView.menu()
        elif option == 3:
            TabletView.menu()
        elif option == 4:
            RegistroDeEmprestimoView.menu()
        else:
            print("Opção inválida. Por favor, insira uma opção válida.")

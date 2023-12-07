from controller.tabletController import AdicionarTablet, AtualizarTablet, ApagarTablet, ListarTablet, BuscarTablet
from controller.livroController import AdicionarLivroController, AtualizarLivroController, ApagarLivroController, ListarLivrosController, BuscarLivroController
from controller.usuarioController import AdicionarUsuario, AtualizarUsuario, ApagarUsuario, ListarUsuario, BuscarUsuario, DevolverUsuario
from controller.registroDeEmprestimoController import AdicionarRegistroLivro, AdicionarRegistroTablet, AtualizarRegistro, ApagarRegistro, ListarRegistro, BuscarRegistroPorID, Multa
from datetime import date, timedelta, datetime

if __name__ == '__main__':
    
    print('************LIVRO***********')
    #Adicionar
    print("====Adicionar livro=====")
    AdicionarLivroController.post("Livro Teste4", "2023-01-04", 987, "Autor Teste4", "Editora Teste4")
    AdicionarLivroController.post("Livro Teste4", "2023-01-04", 987, "Autor Teste4", "Editora Teste4")
    ListarLivrosController.get()
    
    #Buscar
    print("\n====Buscar livro=====")
    BuscarLivroController.get(2)

    print("\n====Listar livro=====")
    ListarLivrosController.get()
    
    #Atualizar
    print("\n====Atualizar livro=====")
    AtualizarLivroController.get(2, "livro editado", datetime.now(), 9, "autor editado", "editora editado", 1)
    ListarLivrosController.get()
    BuscarLivroController.get(2)
    
    print('\n************TABLET***********')
    #Adicionar
    print("====Adicionar Tablet=====")
    AdicionarTablet.post("Tablet A", "2023-11-13", "Marca A", 456)
    AdicionarTablet.post("Tablet B", "2023-11-14", "Marca B", 457)
    AdicionarTablet.post("Tablet C", "2023-11-15", "Marca C", 458)
    
    #Buscar
    print("\n====Buscar Tablet=====")
    BuscarTablet.get(2)

    print("\n====Listar Tablet=====")
    ListarTablet.get()
    
    #Atualizar
    print("\n====Atualizar Tablet=====")
    AtualizarTablet.get(2, "nome editado", datetime.now(), "marca editada", 9, 0) 
    ListarTablet.get()
    BuscarTablet.get(2)

    print('\n************USUARIO***********')
    #Adicionar produtos na base de dados usando nome e preco
    print('====Adicionar Usuario====')
    AdicionarUsuario.post("Berg", 82, 1)
    AdicionarUsuario.post("George", 13, 1)
    ListarUsuario.get()#listo a base de dado

    print('\n====Buscar Usuario====')
    BuscarUsuario.get(2)

    print('\n====Listar Usuario====')
    ListarUsuario.get()

    print('\n====Atualizar Usuario====')
    AtualizarUsuario.get(2)
    DevolverUsuario.get(2)
    ListarUsuario.get()
    BuscarUsuario.get(2)

    #Adicionar novo registro
    print('\n************REGISTRO***********')
    print('====Adicionar Registro====')
    dataInicio = date.today()
    dataFinal = dataInicio + timedelta(7)
    AdicionarRegistroLivro.post(1, 2, dataInicio, dataFinal)
    AdicionarRegistroLivro.post(1, 1, dataInicio, dataFinal)
    AdicionarRegistroTablet.post(2, 3, dataInicio, dataFinal)
    ListarRegistro.get()
    
    print('\n====Atualiza Registro====')
    AtualizarRegistro.get(1, 0)

    print('\n====Busca Registro====')
    BuscarRegistroPorID.get(1)

    print('\n====Listar Registro====')
    ListarRegistro.get()

    data1 = date.today()
    data = data1 + timedelta(14)
    Multa.get(1, data)

    print('\n====Multa Usuario====')
    ListarUsuario.get()

    print('\n************EXCLUIR***********')
    #Excluir
    print('\n====Excluir Registro====')
    ApagarRegistro.get(1)
    ListarRegistro.get()
    print("\n====Apagar Livro=====")
    ApagarLivroController.get(1)
    ListarLivrosController.get()
    print("\n====Apagar Tablet=====")
    ApagarTablet.get(2)
    ListarTablet.get()
    print('\n====Excluir Usuario====')
    ApagarUsuario.get(1)
    ListarUsuario.get()
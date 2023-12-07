from model.livrosModel import Livro

class AdicionarLivroController:
    @staticmethod
    def post(nome, data, codigo_titulo, autor, editora):
        livro = Livro(nome, data, codigo_titulo, autor, editora)
        livro.inserir()

class AtualizarLivroController:
    @staticmethod
    def get(id, nome, data, codigo_titulo, autor, editora, status):
        livro = Livro.buscar_por_id(id)
        livro.setNome(nome)
        livro.setData(data)
        livro.setCodigoTitulo(codigo_titulo)
        livro.setAutor(autor)
        livro.setEditora(editora)
        livro.setStatus(status)
        livro.alterar()

class ApagarLivroController:
    @staticmethod
    def get(id):
        livro = Livro.buscar_por_id(id)
        livro.excluir()

class ListarLivrosController:
    @staticmethod
    def get():
        livros = Livro.listar()
        for livro_info in livros:
            print(f"ID: {livro_info[0]}, Nome: {livro_info[1]}, Autor: {livro_info[5]}, Status:{livro_info[3]}")

class BuscarLivroController:
    @staticmethod
    def get(id):
        print( Livro.buscar_por_id(id))

from bd import _executar
from model.materiaisModel import Material

class Livro(Material):
    def __init__(self, nome, data, codigoTitulo, autor, editora, status = 1, id=None):
        super().__init__(nome, data, status)
        self.__codigoTitulo = codigoTitulo
        self.__autor = autor
        self.__editora = editora
        self.__id = id
        self.__nome = nome

        query="CREATE TABLE IF NOT EXISTS livros(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, data TEXT, status NUMERIC, codigoTitulo NUMERIC, autor TEXT, editora TEXT)" #se a tabela produtos ainda não existir, crio uma
        _executar(query)

    def getId(self):
        return self.__id
    
    def setId(self, valor):
        self.__id = valor

    def getCodigoTitulo(self):
        return self.__codigoTitulo
    
    def setCodigoTitulo(self, valor):
        self.__codigoTitulo = valor

    def getAutor(self):
        return self.__autor
    
    def setAutor(self, valor):
        self.__autor = valor

    def getEditora(self):
        return self.__editora
    
    def setEditora(self, valor):
        self.__editora = valor

    def exibir(self):
        # Aqui você pode personalizar a exibição conforme necessário
        return super().exibir()

    def inserir(self):
        query = f"INSERT INTO livros (nome, data, status, codigoTitulo, autor, editora) VALUES ('{self.getNome()}', '{self.getData()}', '{int(self.getStatus())}', '{int(self.getCodigoTitulo())}', '{self.getAutor()}', '{self.getEditora()}')"
        _executar(query)

    def alterar(self):
        query = f"UPDATE livros SET nome='{self.getNome()}', data='{self.getData()}', status='{self.getStatus()}', codigoTitulo='{self.getCodigoTitulo()}', autor='{self.getAutor()}', editora='{self.getEditora()}' WHERE id={self.getId()}"
        _executar(query)

    def excluir(self):
        query = f"DELETE FROM livros WHERE id={self.getId()}"
        _executar(query)

    @staticmethod
    def listar():
        query = "SELECT * FROM livros"
        livros = _executar(query)
        return livros

    @staticmethod
    def buscar_por_id(id):
        query = f"SELECT * FROM livros WHERE id={int(id)}"
        livro = _executar(query)[0]
        livro = Livro(id = livro[0], nome = livro[1], data=livro[2], status=livro[3], codigoTitulo=livro[4],autor=livro[5], editora=livro[6])
        return livro

    # Função para verificar o status do livro
    def verificar_status(self):
        if self.getStatus() == 1:  # Verifica se o status é disponível para empréstimo
            return True
        else:
            return False

    #to string
    def __str__(self):
        return f"'{self.__id}', '{self.__nome}', '{self.__autor}', '{self._status}'"

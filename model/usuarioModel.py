from bd import _executar

class Usuario:
    def __init__(self, nome, idade, tipoDoUsuario, qDeEmprestimo=0, multa=0, id=None):
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__multa = multa
        self.__tipoDoUsuario = tipoDoUsuario  # Correção: Use 1 para aluno e 2 para outro tipo
        self.__qDeEmprestimos = qDeEmprestimo

    query = "CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, idade INTEGER, multa REAL, qDeEmprestimos INTEGER, tipoDoUsuario INTEGER)"
    _executar(query)
    print("Tabela Criada!")

    def getId(self):
        return self.__id
    def setId(self, value):
        self.__id = value
    def getNome(self):
        return self.__nome
    def setNome(self, valor):
        self.__nome = valor
    def getIdade(self):
        return self.__idade
    def setIdade(self, valor):
        self.__idade = valor
    def getMulta(self):
        return self.__multa
    def setMulta(self, valor):
        self.__multa = valor
    def getTipoUsuario(self):
        return self.__tipoDoUsuario
    def setTipoUsuario(self, valor):
        self.__tipoDoUsuario = valor
    def getQDeEmprestimo(self):
        return self.__qDeEmprestimos
    def setQDeEmprestimo(self, valor):
        self.__qDeEmprestimos = valor

    # Inserir
    def cadastrarUsuario(self):
        # Ajuste para inicializar corretamente a quantidade de empréstimos
        if self.__tipoDoUsuario == 1:
            self.__qDeEmprestimos = 2
        elif self.__tipoDoUsuario == 2:
            self.__qDeEmprestimos = 3
        query = f"INSERT INTO usuarios(nome, idade, multa, qDeEmprestimos, tipoDoUsuario) VALUES ('{self.getNome()}', {int(self.getIdade())}, '{float(self.getMulta())}', {int(self.getQDeEmprestimo())}, {int(self.getTipoUsuario())})"
        _executar(query)
        print("Usuário Cadastrado!")

    # Alterar
    def devolver(self):
        self.setQDeEmprestimo(self.getQDeEmprestimo() + 1)
        query = f"UPDATE usuarios SET qDeEmprestimos={int(self.getQDeEmprestimo())} WHERE id={int(self.getId())}"
        _executar(query)
        
    def alterarUsuario(self):
        if self.getQDeEmprestimo() > 0:
            self.setQDeEmprestimo(self.getQDeEmprestimo() - 1)
            query = f"UPDATE usuarios SET qDeEmprestimos={int(self.getQDeEmprestimo())} WHERE id={int(self.getId())}"
            _executar(query)
        else: print("Limite de emprestimos excedido")

    def alterarMultaUsuario(self):
        query = f"UPDATE usuarios SET multa={float(self.__multa)} WHERE id={int(self.getId())}"
        _executar(query)

    # Excluir
    def excluirUsuario(self):
        query = f"DELETE FROM usuarios WHERE id={int(self.getId())}"
        _executar(query)
        print("Usuário deletado!")

    # Listar professores cadastrados.
    @staticmethod
    def listarUsuarios():
        query = "SELECT * FROM usuarios"
        professores = _executar(query)
        return professores

    # Buscar professor pelo ID.
    @staticmethod
    def listarUsuarioPorId(id):
        query = f"SELECT * FROM usuarios WHERE id={int(id)}"
        resultado = _executar(query)[0]
        if resultado:
            usuario = Usuario(
                nome=resultado[1],
                idade=resultado[2],
                multa=resultado[3],
                tipoDoUsuario=resultado[5],
                qDeEmprestimo=resultado[4],
                id=resultado[0]
            )
            return usuario
        else:
            return None

    def __str__(self):
        return f"{self.__id, self.__qDeEmprestimos}"

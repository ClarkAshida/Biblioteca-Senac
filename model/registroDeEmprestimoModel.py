from bd import _executar
from datetime import date, timedelta, datetime
from model.livrosModel import Livro 
from model.tabletsModel import Tablet
from model.usuarioModel import Usuario

class RegistroDeEmprestimo:
    def __init__(self, codigoUsuario, codigoMaterial, dataInicio, dataFinal, status=1, id = None):
        self.__dataInicio= dataInicio
        self.__dataFinal = dataFinal
        self.__codigoUsuario = codigoUsuario
        self.__codigoMaterial = codigoMaterial
        self.__id = id
        self.__status = status

        query = "CREATE TABLE IF NOT EXISTS RegistroDeEmprestimo(id INTEGER PRIMARY KEY AUTOINCREMENT, codigoMaterial INTEGER, codigoUsuario INTEGER, status INTEGER, dataInicio DATE, dataFinal DATE)"
        _executar(query)
   
    def getDataInicio(self):
        return self.__dataInicio
    def setDataInicio(self, valor):
        self.__dataInicio = valor
    
    def getDataFinal(self):
        return self.__dataFinal
    def setDataFinal(self, valor):
        self.__dataFinal = valor

    def getCodigoUsuario(self):
        return self.__codigoUsuario
    def setCodigoUsuario(self, valor):
        self.__codigoUsuario = valor
    
    def getCodigoMaterial(self):
        return self.__codigoMaterial
    def setCodigoMaterial(self, valor):
        self.__codigoMaterial = valor

    def getStatus(self):
        return self.__status
    def setStatus(self, valor):
        self.__status = valor

    def salvar(self):
        livro = Livro.buscar_por_id(self.__codigoMaterial)  # Obtém o livro associado ao códigoMaterial
        usuario = Usuario.listarUsuarioPorId(self.__codigoUsuario)
        if livro.verificar_status() and usuario.getQDeEmprestimo() > 0:
            query = f"INSERT INTO RegistroDeEmprestimo(codigoMaterial, codigoUsuario, status, dataInicio, dataFinal) VALUES ('{int(self.__codigoMaterial)}', '{int(self.__codigoUsuario)}','{self.__status}', '{self.__dataInicio}', '{self.__dataFinal}')"
            _executar(query)
            usuario.alterarUsuario()
        else:
            print(f"O livro está: {livro.verificar_status()} e a quantidade de empréstimos do usuário está: {usuario.getQDeEmprestimo()}")

    def salvar_tablet(self):
        tablet = Tablet.buscar_por_id(self.__codigoMaterial)  # Obtém o livro associado ao códigoMaterial
        if tablet.verificar_status():
            query = f"INSERT INTO RegistroDeEmprestimo(codigoMaterial, codigoUsuario, status, dataInicio, dataFinal) VALUES ('{int(self.__codigoMaterial)}', '{int(self.__codigoUsuario)}','{self.__status}', '{self.__dataInicio}', '{self.__dataFinal}')"
            _executar(query)
        else:
            print("O Tablet não está disponível para empréstimo.")


    def alterar(self):
        query = f"UPDATE RegistroDeEmprestimo SET status = {int(self.__status)} WHERE id = {int(self.__id)}"
        _executar(query)
        
    def excluir(self):
            query = f"DELETE FROM RegistroDeEmprestimo WHERE id = {int(self.__id)}"
            _executar(query)

    @staticmethod
    def valorMulta( id, data):
        registro = RegistroDeEmprestimo.buscar_por_id(id)
        dataFinal = registro.getDataFinal()
        idUsuario = Usuario.listarUsuarioPorId(registro.getCodigoUsuario())
        if isinstance(dataFinal, str):
            dataFinal = datetime.strptime(dataFinal, '%Y-%m-%d').date()
        if data > dataFinal:
            diasAtraso = (data - dataFinal).days
            multa = float(diasAtraso * 2)
            idUsuario.setMulta(multa)
            idUsuario.alterarMultaUsuario()
            return f"Multa atual: R$ {multa}"
        else:
            return 0

    @staticmethod
    def buscar_por_id(id):
        query = f"SELECT * FROM RegistroDeEmprestimo WHERE id={int(id)}"
        registro = _executar(query)[0]
        registro = RegistroDeEmprestimo(id=registro[0], codigoMaterial=registro[1], codigoUsuario=registro[2], status=registro[3], dataInicio=registro[4], dataFinal=registro[5])

        return registro

    @staticmethod
    def get_registros():
        query = f"SELECT * FROM RegistroDeEmprestimo"
        registros = _executar(query)
        return registros  
    
    def __str__(self):
        return f"{self.__codigoMaterial}, {self.__status}"

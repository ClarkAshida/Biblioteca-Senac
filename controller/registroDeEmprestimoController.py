from model.registroDeEmprestimoModel import RegistroDeEmprestimo

class AdicionarRegistroLivro:
    @staticmethod
    def post(codigoUsuario, codigoMaterial, dataInicio, dataFinal):
        registro = RegistroDeEmprestimo(codigoUsuario, codigoMaterial,dataInicio, dataFinal)
        registro.salvar()

class AdicionarRegistroTablet:
    @staticmethod
    def post(codigoUsuario, codigoMaterial, dataInicio, dataFinal):
        registro = RegistroDeEmprestimo(codigoUsuario, codigoMaterial,dataInicio, dataFinal)
        registro.salvar_tablet()

class AtualizarRegistro:
    @staticmethod
    def get(id, status):
        registro = RegistroDeEmprestimo.buscar_por_id(id)
        registro.setStatus(status)
        registro.alterar()

class ApagarRegistro:
    @staticmethod
    def get(id):
        registro = RegistroDeEmprestimo.buscar_por_id(id)
        registro.excluir()

class ListarRegistro:
    @staticmethod
    def get():
        print(RegistroDeEmprestimo.get_registros())

class BuscarRegistroPorID():
    @staticmethod
    def get(id):
        registro = RegistroDeEmprestimo.buscar_por_id(id)
        print(registro)

class Multa():
    @staticmethod
    def get(id, data):
        multaRegistro = RegistroDeEmprestimo.valorMulta(id, data)
        print(multaRegistro)
from model.usuarioModel import Usuario

class AdicionarUsuario:
    @staticmethod
    def post(nome, idade, tipoDeUsuario):
        usuario = Usuario(nome, idade, tipoDeUsuario)
        usuario.cadastrarUsuario()

    #pegar
class AtualizarUsuario:
    @staticmethod
    def get(id):
        usuario = Usuario.listarUsuarioPorId(id)
        usuario.alterarUsuario()
        print(usuario)

class DevolverUsuario:
    @staticmethod
    def get(id):
        usuario = Usuario.listarUsuarioPorId(id)
        usuario.devolver()
        print(usuario)

class ApagarUsuario:
    @staticmethod
    def get(id):
        usuario = Usuario.listarUsuarioPorId(id)
        usuario.excluirUsuario()

class ListarUsuario:
    @staticmethod
    def get():
        print(Usuario.listarUsuarios())

class BuscarUsuario:
    @staticmethod
    def get(id):
        print(Usuario.listarUsuarioPorId(id))

from model.tabletsModel import Tablet
from bd import _executar

class AdicionarTablet:
    @staticmethod
    def post(nome, data, marca, codigoModelo):
        tablet = Tablet(nome, data, marca, codigoModelo)
        tablet.salvar()

class AtualizarTablet:
    @staticmethod
    def get(id, nome, data, marca, codigo_modelo, status):
        tablet = Tablet.buscar_por_id(id)
        tablet.setNome(nome)
        tablet.setData(data)
        tablet.setMarca(marca)
        tablet.setCodigoModelo(codigo_modelo)
        tablet.setStatus(status)
        tablet.alterar()
        
class ApagarTablet:
    @staticmethod
    def get(id):
        tablet = Tablet.buscar_por_id(id)
        tablet.detetar()

class ListarTablet:
    @staticmethod
    def get():
        tablets = Tablet.getTablets()
        for tablet in tablets:
            print(f"ID: {tablet[0]}, Nome: {tablet[1]}, Marca: {tablet[4]}, Status: {tablet[3]}")

class BuscarTablet:
    @staticmethod
    def get(id):
        tablet = Tablet.buscar_por_id(id)
        print(tablet)
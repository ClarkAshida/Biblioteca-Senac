from abc import ABC, abstractmethod

class Material(ABC):
    #remover a quantidade
    def __init__(self, nome, data, status):
        self._nome = nome
        self._data = data
        self._status = status
    
    def getNome(self):
        return self._nome
    def setNome(self, valor):
        self._nome = valor
    
    def getData(self):
        return self._data
    def setData(self, valor):
        self._data = valor

    def getStatus(self):
        return self._status
    def setStatus(self, valor):
        self._status = valor

    @abstractmethod
    def exibir(self):
        pass


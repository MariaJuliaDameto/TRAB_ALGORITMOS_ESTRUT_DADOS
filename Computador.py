from abc import ABC, abstractmethod
class Computador(ABC):
    @abstractmethod
    def _init_(self, modelo, preco, cor):
        self.modelo = modelo
        self.preco = preco
        self.cor = cor

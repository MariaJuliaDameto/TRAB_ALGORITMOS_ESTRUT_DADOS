from Computador import Computador

class Desktop(Computador):
    def _init_(self, modelo, preco, cor, potenciaFonte):
        self.modelo = modelo
        self.preco = preco
        self.cor = cor
        self.potenciaFonte = potenciaFonte

    def getConfiguracao(self):
        return f"Modelo: {self.modelo}, Preço: {self.preco},Cor: {self.cor}, Potência da Fonte: {self.potenciaFonte}"

    def cadastrar(self):
        print("As configurações do seu Desktop foram salvas.")

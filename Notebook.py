from Computador import Computador

class Notebook(Computador):
    def _init_(self, modelo, preco, cor, duracaoBateria):
        self.modelo = modelo
        self.preco = preco
        self.cor = cor
        self.duracaoBateria = duracaoBateria

    def getInformacoes(self):
        return f"Modelo: {self.modelo}, Cor: {self.cor}, Preço: {self.preco}, Tempo de Bateria: {self.duracaoBateria}"

    def cadastrar(self):
        print("As configurações do seu notebook foram salvas.")

from Desktop import Desktop
from Notebook import Notebook
from Computador import Computador


desktop = Desktop("NEO 50s i5-12400/8GB/SSD256GB", 4500, "Preto", "500W")
print(desktop.getInformacoes())
desktop.cadastrar()

notebook = Notebook("Dell Latitude 3420 i7/16GB/SSD512M.2", 6000, "PRATA", "12 horas")
print(notebook.getInformacoes())
notebook.cadastrar()

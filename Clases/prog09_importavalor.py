from prog08_pidevalor import PideValor

pc = PideValor("Indica el nombre : ", ciclo = "si", li = 5, ls = 10)
cad = pc.pide_cadena()
print(cad)

pn = PideValor("Indica una calificación : ", ciclo = "si", li = 0, ls = 100)
num = pn.pide_numero()
print(num)

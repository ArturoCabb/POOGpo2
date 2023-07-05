class PideValor(object):
    def __init__(self, letrero, li = 0, ls = 0, ciclo = "no", tipo = "", *args, **kwargs):
        self.letrero = letrero
        self.li = li
        self.ls = ls
        self.ciclo = ciclo.upper()
        self.tipo = tipo

    def __del__(self):
        pass
    
    def error(self):
        input(self.letrero)
    
    def pide_cadena(self):
        while True:
            cad = input(self.letrero)
            if (self.ciclo == "NO"): return cad
            else:
                if (self.li == 0) and (self.ls == 0): return cad
                else:
                    if len(cad) < self.li or len(cad) > self.ls:
                        er = ("Error, la cadena debe estar entre " + 
                                 str(self.li) + " y " + str(self.ls) + " caracteres ...")
                        oe = PideValor(er).error()
                        del oe
                    else: return cad
        # Termina ciclo while True
    # Termina pide cadena

    def pide_numero(self):
        while True:
            cad = input(self.letrero)
            if not cad.isnumeric():
                oe = PideValor("Error, la cadena contiene caracteres no validos ...").error()
                del oe
            else:
                if self.tipo == "int" : numero = int(cad)
                else: numero = float(cad)
                if self.ciclo == "NO": return numero
                else:
                    if (self.li == 0) and (self.ls == 0): return numero
                    else:
                        if numero < self.li or numero > self.ls:
                            er = ("Error, valores fuera de rango entre " + str(self.li) + 
                                  " y "+ str(self.ls) + " ...")
                            oe = PideValor(er).error()
                            del oe
                        else: return numero

# Termina PideValor

#pv = PideValor("Indica una cadena : ", ciclo = "si", li = 5, ls = 10)
#cad = pv.pide_cadena()
#pn = PideValor("Indica un numero : ", tipo = "int", ciclo = "si", li = 0, ls = 100)
#num = pn.pide_numero()
#print(num)

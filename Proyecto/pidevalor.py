class PideValor(object):
    def __init__(self, letrero, li = 0, ls = 0, tipo = "", *args, **kwargs):
        self.letrero = letrero
        self.li = li
        self.ls = ls
        self.tipo = tipo

    def __del__(self):
        pass
    
    def error(self):
        input(self.letrero)
    
    def pide_cadena(self):
        while True:
            cad = input(self.letrero)
            if len(cad) == 0 or len(cad) > self.ls:
                er = ("Error, la cadena debe estar entre " + str(self.ls) + " caracteres ...")
                oe = PideValor(er).error()
                del oe
            if self.li == 0 and self.ls == 5:
                if len(cad) != 5:
                    er = ("Error, la cadena debe estar entre " + str(self.ls) + " caracteres ...")
                    oe = PideValor(er).error()
                    del oe
                else: return cad
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
                if (self.li == 0) and (self.ls == 0): return numero
                else:
                    if numero == 0 or numero > self.ls:
                        er = ("Error, valores fuera de rango entre " + str(self.li) + 
                              " y "+ str(self.ls) + " ...")
                        oe = PideValor(er).error()
                        del oe
                    else: return numero
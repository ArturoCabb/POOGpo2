class Computadora():
    def __init__(self, dd = "N/A", mem = "N/A", pro = "N/A", mon = "N/A"):
        self.dd = dd
        self.mem = mem
        self.pro = pro
        self.mon = mon

    def __del__(self):
     pass

    def despliega(self):
        print("Disco Duro :",self.dd)
        print("Memoria    :",self.mem)
        print("Procesador :",self.pro)
        print("Monitor    :",self.mon)

mod1 = Computadora(mem = "8 GB RAM", pro = "Core i3 de 1.2 GHz", mon = "14\" NO TOUCH")
mod1.despliega()
mod2 = Computadora(dd = "500 Gb", mem = "12 Gb", pro="Core i5 de 1.8 GHz", mon="14\" Si Touch")
del mod2
mod2.despliega()

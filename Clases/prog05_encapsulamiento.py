class Computadora():
    def __init__(self, dd = "N/A", mem = "N/A", pro = "N/A", mon = "N/A"):
        self.__dd = dd
        self.mem = mem
        self.pro = pro
        self.mon = mon

    def __del__(self):
     pass

    def despliega(self):
        self.__dd = "12345" # Si se modifica porque está dentro de la misma clase
        print("Disco Duro :",self.__dd) #Al poner el doble guión bajo se imprime el valor agregado principalmente y no el cambio
        print("Memoria    :",self.mem)
        print("Procesador :",self.pro)
        print("Monitor    :",self.mon)

mod1 = Computadora(mem = "8 GB RAM", pro = "Core i3 de 1.2 GHz", mon = "14\" NO TOUCH")
mod2 = Computadora(dd = "500 Gb", mem = "12 Gb", pro="Core i5 de 1.8 GHz", mon="14\" Si Touch")
mod1.despliega()
mod2.__dd = "jajaja"
mod2.despliega()

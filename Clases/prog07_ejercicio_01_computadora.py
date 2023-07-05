class Computadora():
    def __init__(self, *args, **kwargs):
        dd = ""
        mem = ""
        pro = ""
        mon = ""

    def despliega(_self):
        print("Disco Duro : ", _self.dd)
        print("Memoria    : ", _self.mem)
        print("Procesador : ", _self.pro)
        print("Monitor    : ", _self.mon)
        print("")
#Termina la clase Computadora

mod1 = Computadora()
mod1.dd= "500 Mb"
mod1.mem = "8 Gb RAM"
mod1.pro = "Core i3 de 1.2 GHz"
mod1.mon = "14\ No Touch"
mod1.despliega()

mod2 = Computadora()
mod2.dd = "1 Tb"
mod2.mem = "16 Gb RAM"
mod2.pro = "Core i7 de 3.4 GHz"
mod2.mon = "17\ Touch"
mod2.despliega()

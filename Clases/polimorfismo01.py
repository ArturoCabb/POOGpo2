class Bebe(object):
    def muestra(self):
        prrint("Tengo un año o menos de edad")

class Menor():
    def muestra(self):
        print("Tengo entre 1 y 17 años")

class Adulto():
    def muestra(self):
        print("Tengo 18 años o más de edad")

p1 = Bebe().muestra()
p2 = Menor().muestra()
p3 = Adulto().muestra()

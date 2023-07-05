class Bebe():
    def muestra(self):
        prrint("Tengo un año o menos de edad")

class Menor():
    def muestra(self):
        print("Tengo entre 1 y 17 años")

class Adulto():
    def muestra(self):
        print("Tengo 18 años o más de edad")

def muestraEdad(objecto):
    objecto.muestra()

p1 = Bebe()
muestraEdad(p1)
p1 = Menor()
muestraEdad(p1)
p1 = Adulto()
muestraEdad(p1)
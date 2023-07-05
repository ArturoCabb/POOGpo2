from prog08_pidevalor import PideValor

class Persona(object):
    def __init__(self, nom, ap, edad):
        self.__nom = nom
        self.ap = ap
        self.edad = edad

    def __del__(self):
        pass

    def muestra(self):
        print("Nombre    :", self.__nom)
        print("Apellidos :", self.ap)
        print("Edad      :", self.edad)
# Termina clase Persona

class Estudiante(Persona):
    def __init__(self, mat, nom, ap, edad, car):
        self.mat = mat
        self.car = car
        #Dentro de la clase estudiante ejecuta el constructor de la clase Persona
        super().__init__(nom, ap, edad)

    def muestra(self):
        print("Matrícula :", self.mat)
        super().muestra()
        print("Carrera   :", self.car)
# Termina la clase estudiante

pc = PideValor("Indica el nombre     : ", li = 1, ls = 15, ciclo = "si")
nom = pc.pide_cadena()
pc = PideValor("Indica el Ap. Paterno: ", li = 1, ls = 15, ciclo = "si")
pa = pc.pide_cadena()
pn = PideValor("Indica la edad       : ", li = 1, ls = 100, ciclo = "si", tipo = "int")
edad = pn.pide_cadena()
pc = PideValor("Indica la matricula  : ", li = 9, ls = 9, ciclo = "si")
mat = pc.pide_cadena()
pc = PideValor("Indica la Carrera    : ", li = 2, ls = 4, ciclo = "si")
car = pc.pide_cadena()

oe = Estudiante(mat, nom, pa, edad, car).muestra()

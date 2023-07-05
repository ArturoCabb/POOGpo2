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

#op = Persona("Juan", "Pérez López", 25).muestra()
oe = Estudiante("A01369947", "Juan", "Pérez López", 25, "ITC").muestra()

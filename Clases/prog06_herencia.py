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
    pass

persona1 = Persona("Juan", "Pérez López", 15)
persona1.muestra()

estudiante1 = Estudiante("Pancho", "Estudiante Reyes", 10)
estudiante1.muestra()

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
        super().muestra()
        if self.mat != "" and self.car != "":
            print("Matrícula :", self.mat)
            super().muestra()
            print("Carrera   :", self.car)
# Termina la clase estudiante

class Deportista(Estudiante):
    def __init__(self, mat, nom, ap, edad, car, deporte):
        self.deporte = deporte
        super().__init__(mat, nom, ap, edad, car)

    def muestra(self):
        super().muestra()
        print("Deporte   :", self.deporte)
# Termina la clase Deportista

class Tallerista(Estudiante):
    def __init__(self, mat, nom, ap, edad, car, taller):
        self.taller = taller
        super().__init__(mat, nom, ap, edad, car)
    def muestra(self):
        super().muestra()
        print("Taller    :", self.taller)
# Termina la clase Tallerista

#od = Deportista("A01366123", "Juan", "Pérez", "25", "ITC", "Básquetbol").muestra()
#ot = Tallerista("A01366123", "Juan", "Pérez", "25", "ITC", "Danza").muestra()
od_persona = Deportista("", "Juan", "Pérez", "25", "", "Atletismo").muestra()

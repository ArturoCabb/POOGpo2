class Persona():
    def __init__(self, nom, ap, am, edad):
        self.nom = nom
        self.ap = ap
        self.am = am
        self.edad = edad

    def muestra(self):
        print("Nombre           :", self.nom)
        print("Apellido paterno :", self.ap)
        print("Apellido materno :", self.am)
        print("Edad             :", self.edad)
#Termina clase persona

class Estudiante(Persona):
    def __init__(self, nom, ap, am, edad, mat, car):
        self.mat = mat
        self.car = car
        super().__init__(nom, ap, am, edad)

    def muestra(self):
        if self.mat != "" and self.car != "":
            print("Matricula        :", self.mat)
            print("Carrera          :", self.car)
        super().muestra()

class Deportista(Estudiante):
    def __init__(self, nom, ap, am, edad, mat, car, deporte, taller):
        self.deporte = deporte
        super().__init__(nom, ap, am, edad, mat, car, taller)

    def muestra(self):
        super().muestra()
        if self.deporte != "":
            print("Deporte          :", self.mat)

class Tallerista(Estudiante):
    def __init__(self, nom, ap, am, edad, mat, car, taller):
        self.taller = taller
        super().__init__(nom, ap, am, edad, mat, car)

    def muestra(self):
        super().muestra()
        if self.taller != "":
            print("Taller           :", self.taller)

class Todas(Deportista, Tallerista):
    pass

#pe = Deportista("Juan", "Perez", "Lopez", 25, "A01366123", "ITC", "Básquetbol").muestra()
#print("--------------------------------------------------------")
#to = Todas("Juan", "Perez", "Lopez", 25, "A01366123", "ITC", "Básquetbol", "Teatro").muestra()
print("SOLO PEPRSONA ------------------------------------------")
pe = Todas("Juan", "Perez", "Lopez", 25, "", "", "", "").muestra()
print("ESTUDIANTE Y PERSONA -----------------------------------")
pe = Todas("Pedro", "Ramirez", "Albarran", 15, "A01366123", "ITC", "", "").muestra()
print("ESTUDIANTE, PERSONA Y DEPORTISTA -----------------------")
de = Todas("Pedro", "Ramirez", "Albarran", 15, "A01366123", "ITC", "Básquetbol", "").muestra()
print("ESTUDIANTE, PERSONA Y TALLERISTA -----------------------")
ta = Todas("Francisco", "Reyes", "Días", 18, "A01366123", "ITC", "", "Teatro").muestra()
print("ESTUDIANTE, PERSONA, TALLERISTA Y DEPORTISTA ------------")
ta = Todas("Gabriela", "Perez", "Lopez", 25, "A01366123", "ITC", "Tocho Bandera", "Guitarra").muestra()

from pidevalor import *
from files import *

class Video():
    def __init__(self):
        self.id = ""
        self.titulo = ""
        self.duracion = ""
        self.calificacion = ""

    def __del__(self):
        pass

    def validacion(self, x):
        if  x[0] == ("P" or "S" or "D"):
            pass
        else: print("Error en el tipo de video")
        if x[1] == ("A" or "B" or "C" or "D"):
            pass
        else: print("Error en la clasificación")
        try:
            if int(x[2:]) == int():
                pass
        except e:
            print("Error ", e)

    def pide_datos(self):
        self.id = PideValor("Ingrese el ID del video: ", ls = 5).pide_cadena()
        self.titulo = PideValor("Ingrese el Titulo del video: ", li = 1, ls = 30).pide_cadena()
        self.duracion = PideValor("Ingrese la duracion del video: ", li = 1, ls = 500, tipo = "int").pide_numero()
        self.calificacion = PideValor("Ingrese la calificación del video: ", li = 1, ls = 5, tipo = "int").pide_numero()
        Video().validacion(self.id)

    def muestra_datos(self, dato):
        self.id = dato[0]
        self.titulo = dato[1]
        self.duracion = dato[2]
        self.calificacion = dato[3]
        print("ID del video -> ", self.id)
        print("Titulo del video -> ", self.titulo)
        print("Duración del video -> ", self.duracion)
        print("Calificación del video -> ", self.calificacion)

class Peliculas(Video):
    def __init__(self):
        super().__init__()
        self.audencia = ""
        self.genero = ""

    def pide_datos(self):
        super().pide_datos()
        self.audencia = PideValor("Ingrese la audencia de la película: ", li = 1, ls = 15).pide_cadena()
        self.genero = PideValor("Ingrese el genero de la película: ", li = 1, ls = 15).pide_cadena()
        cadena = self.id + self.titulo + "," + self.genero + "," + str(self.duracion) + "," + str(self.calificacion) + "," + self.audencia + "," + "," + "," + ","
        Archivo().buscar(cadena, "P", self.id)

    def muestra_datos(self, dato):
        self.audencia = dato[4]
        self.genero = dato[5]
        super().muestra_datos(dato)
        print("Audencia de la Película -> ", self.audencia)
        print("Género de la Película -> ", self.genero)

class Serie(Peliculas):
    def __init__(self):
        super().__init__()
        self.temporada = ""
        self.episodio = ""
        self.tit_episodio = ""

    def pide_datos(self):
        super().pide_datos()
        self.temporada = PideValor("Ingrese la temporada de la serie: ", li = 1, ls = 500, ciclo = "si").pide_numero()
        self.episodio = PideValor("Ingrese el episodio de la serie: ", li = 1, ls = 500, ciclo = "si").pide_numero()
        self.tit_episodio = PideValor("Ingrese el titulo del episodio: ", li = 1, ls = 30, ciclo = "si").pide_cadena()
        cadena = self.id + self.titulo + "," + self.genero + "," + str(self.duracion) + "," + str(self.calificacion) + "," + self.audencia + "," + str(self.temporada) + "," + str(self.episodio) + "," + self.tit_episodio + ","
        Archivo().buscar(cadena, "P", self.id)


    def muestra_datos(self, dato):
        self.temporada = dato[6]
        self.episodio = dato[7]
        self.tit_episodio[8]
        super().muestra_datos(dato)
        print("Temporada de la serie -> ", self.temporada)
        print("Episodio de la serie -> ", self.episodio)
        print("Título del episodio de la serie -> ", self.tit_episodio)

class Documental(Serie):
    def __init__(self):
        super().__init__()
        self.tema = ""

    def pide_datos(self):
        super().pide_datos()
        self.tema = PideValor("Ingrese el tema del documental: ", li = 1, ls = 30, ciclo = "si").pide_cadena()
        cadena = self.id + self.titulo + "," + self.genero + "," + str(self.duracion) + "," + str(self.calificacion) + "," + self.audencia + "," + str(self.temporada) + "," + str(self.episodio) + "," + self.tit_episodio + "," + self.tema
        Archivo().buscar(cadena, "P", id)


    def muestra_datos(self, dato):
        self.tema = dato[9]
        super().muestra_datos(dato)
        print("Tema del documental -> ", self.tema)

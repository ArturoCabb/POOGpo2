# -*- coding: utf-8 -*-
import pidevalor
from videos import *
from files import *
import os

if __name__ == "__main__":
    while 1:
        print("*"*20, " Menú Principal ", "*"*20)
        print("1) Agregar Videos")
        print("2) Consultar video por ID")
        print("3) Consultar video por Título")
        print("4) Consultar video por Género")
        print("5) Listado General")
        print("6) Listado de Películas")
        print("7) Listado de Series")
        print("8) Listado de Documentales")
        print("9) Listado por Calificaciones")
        print("10) Salir")
        print("*"*56)
        i = int(input())
        if i == 1:
            print("¿Qué video quiere? \n\rP) Para Película \n\rS) Para Serie \n\rD) Para Documental\n\r")
            opcion = input().upper()
            if opcion == "P":
                Peliculas().pide_datos()
            elif opcion == "S":
                Series().pide_datos()
            elif opcion == "D":
                Documental.pide_datos()
        elif i == 2:
            consulta = PideValor("Ingrese el ID: ", ls = 5).pide_cadena()
            o = Archivo().buscar("", "CID", consulta)
            if consulta[0] == "P":
                Peliculas().muestra_datos(o)
            elif consulta[0] == "S":
                Peliculas().muestra_datos(o)
            elif consulta[0] == "D":
                Peliculas().muestra_datos(o)
        elif i == 3:
            consulta = PideValor("Ingrese el Titulo: ", ls = 30).pide_cadena()
            Listados().general(3,texto = consulta)
        elif i == 4:
            consulta = PideValor("Ingrese el Genero: ", ls = 15).pide_cadena()
            Listados().general(4, texto = consulta)
        elif i == 5:
            Listados().general(5)
        elif i == 6:
            Listados().general(6)
        elif i == 7:
            Listados().general(7)
        elif i == 8:
            Listados().general(8)
        elif i == 9:
            limite1 = PideValor("Ingrese un límite inferior: ").pide_numero()
            limite2 = PideValor("Ingrese un límite superior: ").pide_numero()
            Listados().general(9, n1 = limite1, n2 = limite2)
        elif i == 10:
            break


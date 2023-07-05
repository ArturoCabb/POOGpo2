class Persona():
    nom = "Juan"
    ap = "Pérez"
    am = "López"
    edad = 25

    def muestra(_self):
        print("Nombre      :",_self.nom)
        print("Ap. Paterno :",_self.ap)
        print("Ap. Materno :",_self.am)
        print("Edad        :",_self.edad)
        print("")
#Termina la clase Persona

juan = Persona()
juan.muestra()

pedro = Persona() # Se crea el objeto "pedro" como instancia de la clase Persona
pedro.nom = "Pedro" # Cambia el valor del atributo "nom" a través del objeto pedro
pedro.ap = "Jiménez"
pedro.am = "Rojas"
pedro.edad = 50
pedro.muestra()

luis = Persona()
luis.nom = "Luis"
luis.muestra()

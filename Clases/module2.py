class Persona():
     def __init__(self,nombre,apellidos,edad):
         self.nombre=nombre # Guiones bajos en el nombre
         self.apellidos=apellidos
         self.edad=edad

     def muestra(self):
         print("Nombre : ",self.nombre)
         print("Apellidos : ",self.apellidos)
         print("Edad : ",self.edad)

     def __str__(self):
         cad1="Hola"
         cad2="Bienvenidos"
         return cad2
# Termina la definición de la clase
p1=Persona("Juan","Pérez Reyes",25)
print (p1)
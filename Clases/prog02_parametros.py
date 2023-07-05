def suma(x,y):
    print("x=", x)
    print("y=", y)
    r = x + y
    return r

def suma(z, x = 0,y = 0): # Primero argumentos posicionales y luego argumentos por asignación
    print("x=", x)
    print("y=", y)
    r = x + y
    return r

print("La suma es: ",suma(x=5,y=10))

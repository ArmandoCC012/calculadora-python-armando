#Funcion de suma variable con argumentos
#Crea una funcion que reciba cualquier cantidad de numeros y devuelva su suma y 
# el promedio de esa suma.

def sumarypromedio(*numeros):
    suma=sum(numeros)
    promedio=suma/len(numeros)
    Mensaje=f"La suma es: {suma} y el promedio es:{promedio}"
    return Mensaje
entrada=input("Ingresa n enteros cuales sea ")
numeros1=[int(x) for x in entrada.split()]

SalidaDeDatos=sumarypromedio(*numeros1)
print(SalidaDeDatos)

#Contador de palabras de una frase
"""
Forma recomendada (sin excepciones)
while j < len(ListaDePalabras):
    if ListaDePalabras[j] == True:
        print("")
    j += 1

"""
oracion=input("Ingrese una oracion corta: ")
ListaDePalabras=oracion.split()
diccionariodeLasPalabras={
}
j=int(0)
while True:
    valorDeldic=int(0)
    i=0
    for a in ListaDePalabras: 
        if ListaDePalabras[j]==ListaDePalabras[i]:
            valorDeldic=valorDeldic+1
        i=i+1
    diccionariodeLasPalabras[ListaDePalabras[j]]=valorDeldic
    j=j+1
    try:
        if ListaDePalabras[j]==True:
            print("")
    except IndexError:
        break
print("El diccionario es el siguiente:")
for c,v in diccionariodeLasPalabras.items():
    print("clave:",c,"valor:",v)
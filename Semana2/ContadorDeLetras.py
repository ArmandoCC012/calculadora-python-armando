#Contador De Letras en una Frase
#Usa Dict comprehension
#Clave la Letra,Cantidad el numero de esa letra en la oracion. 
"""listapalabra=input("Ingresa una oracion corta.")
    listapalabra.lower()
##Forma tradicional
ContadordePalabram={}
listasinespacios=[]
for c in listapalabra:
    if c!=" ":
        listasinespacios.append(c)
for c1 in listasinespacios:
    if c1 in ContadordePalabram:
        ContadordePalabram[c1]=ContadordePalabram[c1]+1
    else:
        ContadordePalabram.update({c1:1})
for c,v in ContadordePalabram.items():

    print(c,v)"""
#Forma dic compress
oracion=input("Ingrese una oracion:")
oracion=oracion.lower()
dixxionario={
    C:oracion.count(C) for C in oracion if C != " "}
for c,v in dixxionario.items():
    print(c,v)
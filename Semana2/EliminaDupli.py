#Set
i=0
Lista_Natural=[]
SetNumero=set([])
while i<8:
    try:
        numero=int(input("Ingresa un Numero: "))
    except ValueError:
        print("Introdusca un valor entero")
        continue
    SetNumero.add(numero)
    Lista_Natural.append(numero)
    i=i+1
print("La lista original es:")
print(Lista_Natural)
print("El Set de numeros es:")
print(SetNumero)

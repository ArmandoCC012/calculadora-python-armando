ElMenu={
    "Pizzsa" : 10,
    "Pollo" : 20,
    "Lomito" : 15,
    "PiqueMacho" : 30
}
SetDePlatos=set([])
print("Nuestro Menu contiene lo siguiente:")
for c,v in ElMenu.items():
    SetDePlatos.add(c)
    print(c,"su precio:",v)
print("Que pedira?:")
ValorApagar=int(0)
while(True):
    pedir=input()
    if pedir in SetDePlatos:
        print("")
    else:
        print("El plato no existe ingrese uno del menu")
        continue
    for c in ElMenu.keys():
        if c==pedir:
            ValorApagar=ValorApagar+ElMenu.get(pedir)
    print("¿algo mas?")
    decicion=input("s/n: ")
    if decicion=="n":
        break
print("El valor Total a cancelar es de:",ValorApagar,"Bs")

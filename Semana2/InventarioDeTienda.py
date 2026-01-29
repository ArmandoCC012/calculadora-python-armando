#Inventario de Tienda con actualizacion 
#Crea un diccionario inventario con productos y cantidades:
Frutas={
    'Pera':10,
    'Manzana':200,
    'Tomate':1500,
    'Frutillas':150,
    'Mango':2000,
    'Naranja':3000
}
while(True):
    print("             Bienvenido esta es una tienda de Frutas")
    print("       El listado se muestra a continuacion:" \
"--------------------------------------------------------------------------------" \
"Fruta://Cantidad:")
    i=0
    for c,v in Frutas.items():
        print(i+1,".-",c,v,"")
        i=i+1
    print("Funciones que puede realizar:")
    print("1.-Actualizar la cantidad de un producto.")
    print("2.-Agregar un nuevo producto ala venta")
    print("3.-Salir del programa.")
    opcion=input("¿Que opcion elige?:1/2/3")
    if opcion == '1' or opcion=='2' or opcion=='3':
        if opcion=='1':
            eleccion=input("La fruta es?:")
            if eleccion in Frutas:
                try:
                    nuevoPrecio=int(input("Nueva cantidad?:"))
                    Frutas[eleccion]=nuevoPrecio
                except ValueError:
                    print("Por favor ingrese un valor entero")
                    pausa=input("Precione cualquier Tecla para continuar")
                    continue
            else:
                print("Debe de Colocar un nombre de la lista")
                pausa=input("Precione cualquier Tecla para continuar")
        elif opcion=='2':
            nuevaFruta=str(input("Que fruta desea agregar?:"))
            if nuevaFruta != int:
                 try:
                    ClaveNFruta=int(input("Su cantidad es?:"))
                    Frutas.setdefault(nuevaFruta,ClaveNFruta)
                 except ValueError:
                    print("coloque una cantidad correcta!")
                    pausa=input("Preciones cualquier Tecla")
            else:
                print("Ingrese un nombre correcto!.")
                pausa=input("Precione cualquier Tecla")
           
        elif opcion=='3':
            break
    else:
        print("Debe de escoger un numero Mayor a 0 o menor a 4.")
        pausa=input("Precione cualquier Tecla")

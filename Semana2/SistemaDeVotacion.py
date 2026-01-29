#Sistema de votacion Simple
#A)  Crear un diccionario, donde la clave sea el CANDIDATO, y el valor sera LA CANTIDAD
#    DE VOTOS QUE RECIVIO DICHO CANTIDATO
#B)  Pedir los nombres de los votantes y para quien sera su voto("El nombre de Cantidato")
#C)  Usa un set(conjunto) para anotar a los votantes y evitar duplicados
#D)  La salida sera; la lista de votantes(set), cantidad de votos que recivieron 
#     los candidatos y por ultimo el nombre de el ganador candidato-votos
listadeVotantes=set([])
i=0
diccionario={}
while i<5:
    #Candidatos a seleccionar
    print("CANDIDATOS: FUENTES" \
    "                  LLANINA" \
    "                  TEODORO" \
    "                  PAMBIA" \
    "                  ZARATA")
    #Entradas
    nombrevotantes=input("Ingrese su Nombre Completo:")
    listadeVotantes.add(nombrevotantes)
    candidatoAvotar=input("Por que candidato votara ingrese el nombre:")
    #Controles
    if candidatoAvotar not in diccionario:
        diccionario.setdefault(candidatoAvotar,1)
    else:
        diccionario[candidatoAvotar]=diccionario[candidatoAvotar]+1
    i=i+1
#Llevar los valor del diccionario a una lista
listaValores=[]
a=int(0)
for c,v in diccionario.items():
    listaValores.append(int(v))
#Encontrar el valor maximo
i=int(0)
ValorMaximo=int(0)
while True:
    j=0
    while True:
        if listaValores[i] > listaValores[j]:
            if ValorMaximo < listaValores[i]:
                ValorMaximo=listaValores[i]
        j=j+1
        if j == len(listaValores):
            break
    i=i+1
    if i == len(listaValores):   
        break
#salida de lista de votantes
print(listadeVotantes)
#Votos que recogieron los candidatos
for c,v in diccionario.items():
    print(c,v)
#Identificar al ganador
for c,v in diccionario.items():
    if v==ValorMaximo:
        print("El ganador de la votacion es: ")
        print(c,v)

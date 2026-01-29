#Funcion Que muestra a los Candidatos
def Candidatos():
    print("CANDIDATOS: FUENTES" \
    "                  LLANINA" \
    "                  TEODORO" \
    "                  PAMBIA" \
    "                  ZARATA")
    #Set para nombres de votantes y lista para anotar Al Candidato
ListaDeCandidatos=[]
NombresV=set([])
#Funcion que guarda el nombre de los votantes y por quien votaron
def RegistroVotantes(nombreV,Candidato):
    NombresV.add(nombreV)
    ListaDeCandidatos.append(Candidato)
#Funcion que muestra A los votantes
def NdeVotantes():
    for V in NombresV:
        print(V)
#Funcion que muestra a los candidatos con sus respectivos votos
def Resultados():
    #Diccionario para los Candidatos y sus respectivos votos
    almacen={x:ListaDeCandidatos.count(x) for x in ListaDeCandidatos}
    print(almacen)
    return almacen
#Funcion que muestra a el ganador 
def Ganador(Dic):
    ganador=max(Dic, key=Dic.get)
    valores=Dic[ganador]
    return {ganador:valores}
Candidatos()
while True:

    print(RegistroVotantes(input("Ingrese su nombre porfavor"),input("A que candidato votara:")))
    print(ListaDeCandidatos)
    de=input("Presione X para salir C para continuar")
    if de == 'x' or de == 'X':
        break
print("Nombres de los votantes:")
NdeVotantes()
print("Resultados de las votaciones:")
Resultados()
print("El ganador es:",Ganador(Resultados()),"Votos Felicidades")
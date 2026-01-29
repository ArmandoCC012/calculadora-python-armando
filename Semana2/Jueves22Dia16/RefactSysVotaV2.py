# Diccionario global de candidatos (inicial en 0)
candidatos = {
    "FUENTES": 0,
    "LLANINA": 0,
    "TEODORO": 0,
    "PAMBIA": 0,
    "ZARATA": 0
}

# Set global para votantes únicos
votantes = set()
#Funcion que muestra a el diccionario con una ennumeracion que comienza de 1 
def mostrar_candidatos():
    print("CANDIDATOS DISPONIBLES:")
    for i, cand in enumerate(candidatos.keys(), 1):
        print(f"{i}. {cand}")
#Funcion que asigna valores a set votantes y a el diccionario candidatos, solo si-
# el candidato es valido y el votante no ha votado
def registrar_voto(nombreV, Ecandidato):
    #Solo registrar un voto si el candidato es valido y el votante no ha votado
    Ecandidato= Ecandidato.upper().strip()
    if Ecandidato not in candidatos:
        print(f"Error: '{Ecandidato}' no es un candidato valido.")
        return False
    if nombreV in votantes:
        print(f"{nombreV} ya voto, Solo se permite un voto por persona")
        return False
    votantes.add(nombreV)
    candidatos[Ecandidato]=candidatos[Ecandidato]+1
#Funcion que imprime los valores del diccionario solo si tienes valores > 0 
def mostrar_resultados():
    print("\nRESULTADOS DE LA VOTACION :")
    for cand, votos in candidatos.items():
        print(f"{cand}, con: {votos}")
    if not any(candidatos.values()):
        return "Aun no pusieron votos"
#Funcion que retorna el mayor valor y su clave del diccionario solo si hay un valor > 0 
def encontrar_ganador():
    if not any(candidatos.values()):
        return "No ay ganador"
    ganador=max(candidatos, key=candidatos.get)
    votos_ganador=candidatos.get(ganador)

    #Chekeo de empate
    ganadores= [c for c,v in candidatos.items() if v==votos_ganador]
    if len(ganadores) > 1:
        return f"Empate entre: {','.join(ganadores)} ({votos_ganador} cada uno)"
    return f"{ganador} con {votos_ganador} votos"
print("____SISTEMA DE VOTACION SIMPLE____")
mostrar_candidatos()
#Ciclo repetitivo para ingresar valores que se almacenaran a el diccionario y el conjunto siempre y cuando,
# las entradas sean correctas; Y decicion de seguir o salir del programa
while True:
    print("---Registrar voto---")
    nombre = input("Tu nombre completo: ").strip()
    if not nombre:
        print("El nombre no puede estar vacio.")
        continue
    candidato =input("Candidato por que votaras?: ").strip()
    registrar_voto(nombre,candidato)
    continuar=input("¿Otro voto? (s/n): ").lower().strip()
    if continuar != 's':
        break
#Resultados finales
print("\n" + "="*40)
print("VOTANTES QUE PARTICIPARON:",",".join(sorted(votantes)) or "ninguno")
mostrar_resultados()
print("\nGANADOR:", encontrar_ganador())
print("="*40)




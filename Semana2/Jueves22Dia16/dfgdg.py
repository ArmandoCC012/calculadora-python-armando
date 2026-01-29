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

def mostrar_candidatos():
    print("CANDIDATOS DISPONIBLES:")
    for i, cand in enumerate(candidatos.keys(), 1):
        print(f"{i}. {cand}")

def registrar_voto(nombre, candidato):
    """
    Registra un voto si el candidato es válido y el votante no ha votado.
    """
    candidato = candidato.upper().strip()  # Normalizamos
    
    if candidato not in candidatos:
        print(f"Error: '{candidato}' no es un candidato válido.")
        return False
    
    if nombre in votantes:
        print(f"{nombre} ya votó. Solo se permite un voto por persona.")
        return False
    
    votantes.add(nombre)
    candidatos[candidato] += 1
    print(f"Voto registrado para {candidato} por {nombre}")
    return True

def mostrar_resultados():
    print("\nRESULTADOS DE LA VOTACIÓN:")
    for cand, votos in candidatos.items():
        print(f"{cand}: {votos} votos")
    
    if not any(candidatos.values()):  # Si no hay votos
        print("Aún no hay votos.")

def encontrar_ganador():
    if not any(candidatos.values()):
        return "Aún no hay votos."
    
    ganador = max(candidatos, key=candidatos.get)
    votos_ganador = candidatos[ganador]
    
    # Chequeo de empate
    ganadores = [c for c, v in candidatos.items() if v == votos_ganador]
    if len(ganadores) > 1:
        return f"Empate entre: {', '.join(ganadores)} ({votos_ganador} votos cada uno)"
    return f"{ganador} con {votos_ganador} votos"

# Programa principal
print("=== SISTEMA DE VOTACIÓN SIMPLE ===")
mostrar_candidatos()

while True:
    print("\n--- Registrar voto ---")
    nombre = input("Tu nombre completo: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        continue
    
    candidato = input("Candidato por el que votas: ").strip()
    
    registrar_voto(nombre, candidato)
    
    continuar = input("\n¿Otro voto? (s/n): ").lower().strip()
    if continuar != 's':
        break

# Resultados finales
print("\n" + "="*40)
print("VOTANTES QUE PARTICIPARON:", ", ".join(sorted(votantes)) or "Ninguno")
mostrar_resultados()
print("\nGANADOR:", encontrar_ganador())
print("="*40)
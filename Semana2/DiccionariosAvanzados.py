diccionario1={
    'pepito':854,
    'valor':34,
    'Jorgito':0
}
diccionario2={
    'tiita':200,
    'Jorgito':4000
}
Yolo=diccionario1
# update Combinar diccionarios
diccionario1.update(diccionario2)
# setdefault Agregar una clave-valor solo si no existe la clave
diccionario1.setdefault('pepita',"bonito")
#Salida de datos
print(Yolo)
##Usos en Contadores y agrupaciones
 #Lista de Votaciones
Votantes=['Teodoro','Llamila','Araceli','Tia','Teodoro','Tia','Teodoro']
NumeroDeVotacionesDeVotantes={}
for c in Votantes:
    NumeroDeVotacionesDeVotantes.setdefault(c,0)
    NumeroDeVotacionesDeVotantes[c]=NumeroDeVotacionesDeVotantes[c]+1
print(NumeroDeVotacionesDeVotantes)
##Dict Comprehension: Uso de Bucles y Condicionales dentro de los diccionario.
##{clave: valor for elemento in iterable}
#Forma Tradicional Usando bucle
numeros={'a':1,'b':2,'c':3}
doble={}
for c,v in numeros.items():
    doble.setdefault(c,v*2)
print(doble)
#Forma Dict Comprehension usando blucle
numeros1={'a':1,'b':2,'c':3}
doble1={K:V*3 for K,V in numeros1.items()}
print(doble1)
#Forma Tradicional usando Condicionales
enteros={'1':1,'2':2,'3':3,'4':4,'5':5}
numerosPares={}
for c,v in enteros.items():
    if enteros[c]%2==0:
        numerosPares.setdefault(c,v)
print(numerosPares)
#Forma Dict Comprehension usando Condicion
enteros1={'1':6,'2':7,'3':8,'4':9,'5':10}
numerosPares1={K1:V1 for K1,V1 in enteros1.items() if V1%2==0}
print(numerosPares1)

#Set Comprehension.- Crear sets en una línea, usando bucles y condicionales.
#{expresion for elemento in iterable if condicion}
lista1=[-4,-89,-100,-4,5,7,-89,-10,7,5,12,20]
ConjuntoDeNumerosPositivosQuePertenecenaLista1={p for p in lista1 if p>0}
print(ConjuntoDeNumerosPositivosQuePertenecenaLista1)


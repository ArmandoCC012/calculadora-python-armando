#Registro de Estudiantes
notasyedadA={"Edad":20,"Notas":85}
notasyedadB={"Edad":19,"Notas":88}
notasyedadT={"Edad":20,"Notas":90}
notasS={"Edad":21,"Notas":100}
Estudiantes_De_Primero ={

    "Arnold": notasyedadA,
    "Baby": notasyedadB,
    "Tia": notasyedadT,
    "Selma": notasS
}
NotaTotal=int(0)
CantidadNotas=int(0)
for c,v in Estudiantes_De_Primero.items():
    NotaTotal=NotaTotal+Estudiantes_De_Primero[c].get("Notas")
    CantidadNotas=CantidadNotas+1
promedio=NotaTotal/CantidadNotas
print("El promedio de las notas de los estudiante es de:",promedio)
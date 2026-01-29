def promedo_De_Notas(*notitas):
    if not notitas:
        return "Lo siento al parecer no ingreso numeros" 
    promedio=sum(notitas)/len(notitas)
    return promedio
promedioDeEntero=promedo_De_Notas(0,1,2,3,4,5,6,7,8,9)
print(promedioDeEntero)
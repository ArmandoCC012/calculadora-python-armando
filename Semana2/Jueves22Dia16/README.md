# 1. Parametros por defecto.-
    Son Valores que una funcion usa si no le pasas nada.
    *Sintaxis: def saludo(nombre="soy por defecto"):
                    print(f"Eres,{nombre}")
    *Uso:       saludo("Armando") #Salida "Eres, Armando"
                saludo()          #Salida "Eres, soy por defecto"
    *Regla: Los parametros con Valores deben ir al final.
                def MAL(a=0,b):
                def BIEN(a,b=0): 
# 2. *args (Argumentos variables)
    Permiten que una funcion reciba cualquier cantidad de argumentos
    *Sintaxis: def suma(*numero):
                return sum(numeros)
    *Uso:       print(suma(1,2))   #Salida 3
                print(suma(1,2,3,4,5)) #Salida 15
    *¿Que es numero?: * convirtio a numero en una TUPLA numero es lo mismo que tupla=(1,3)
    *Cuando se usa: Cuando no sabes cuantos valores te pasaran. 
                    -Ejemplo: Votos,notas,precios,numeros ingresados por usuario.
# 3. **kwargs (argumentos con nombre variables)
    Permite recibir muchos argumentos con nombre(clave=valor)
    *Sintaxis: def semidic(**datasos):
                print(datasos)
    *Uso:       semidic(pepito=18,sambrana=10,tionacho=20)
    *¿Que es datasos?: ** convirio a datasos en un DICCIONARIO; 
                                    datasos={pepito=18,sambrana=10}
# 4. *args + **kwargs JUNTOS
    *Orden de uso:  1. parametros normales
                    2. *args
                    3. **kwargs
    *Ejemplos de usos:  def ejem(li,*tupla,**diccio):
                            print(f"***{li}***")
                            print(f"La tupla es de {tupla}")
                            print(f"El diccionario es:{diccio}")
                        ejem("Menu de Inicio",1,2,3,Entrada='E',Proceso='P',Salida='S')
                        #Salida ***Menu de Inicio***
                            La tupla es de (1,2,3)
                            El diccionario es:{'Entrada':'E','Proceso'='P','Salida'='S'}
# 5. Funciones lambda
    Una funcion corta, anonima, de una sola linea.
    *Sintaxis:  lambda argumentos: expresion
    *Ejemplo: cuadrado= lambda x: x**2
                print(cuadrado(5)) #Salida 25
    *Equivalencia-forma normal del Ejemplo:
                def cuadrado(x):
                    return x**2
    *¿Cuando usar lambda?:
        -En funciones pequeñas
        -Usar con map(),filter(),sorted() #sorted() Ordena lista
        -NO PARA LOGICA COMPLETA
    *Ejemplo Real:
        numero=[1,2,3,4,5]
        cuadrados=list(map(lambda x: x**2,numero))
        pares=list(filter(lambda x: x%2==0,numero)) 
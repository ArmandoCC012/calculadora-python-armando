#Operaciones Aritmeticas Basicas  con menu de opciones
def Operaciones(a,o,b):
    if o=="+":
        return a+b
    elif o=="-":
        return a-b
    elif o=="*":
        return a*b
    elif o=="/":
        if b!=0 and a!=0:
            return a/b
        else:
            return "Error: Division por cero"
    else:
        return "Operador no valido"
print("MENU DE OPERACIONES ARITMETICAS BASICAS")
while True:
    print("Por favor inserte los numero mas el operador")
    try:
        num1=float(input())
    except ValueError:
        print("Error: Entrada no valida. Por favor ingrese un numero.")
        continue
    try:
        operador=input()
        if(operador == "+" or operador == "-" or operador == "*" or operador == "/"):
            pass
    except ValueError:
        print("Error de concurrencia. Intente de nuevo.")
        continue
    try:
        num2=float(input())
    except ValueError:
        print("Error: Entrada no valida. Por favor ingrese un numero.")
        continue
    resultado=Operaciones(num1,operador,num2)
    print("El resultado es:",resultado)
    print("Desea realizar otra operacion? (s/n)")
    respuesta=input()
    if respuesta !="s":
        break
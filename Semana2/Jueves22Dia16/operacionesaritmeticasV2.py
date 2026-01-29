#Operaciones Aritmeticas Basicas  con menu de opciones
def Operaciones(a,o,b):
    operadores={
        '+': lambda x,y: x+y,
        '-': lambda x,y: x-y,
        '*': lambda x,y: x*y,
        '/': lambda x,y: x/y
    }
    if o in operadores:
        if o == '/' and a!=0 and b!=0:
            return operadores[o](a,b)
        elif o!='/':
            return operadores[o](a,b)
        else:
            return "No se puede dividir por 0"
    """if o=="+":
        return a+b
    elif o=="-":
        return a-b
    elif o=="*":
        return a*b
    elif o=="/":
        if b!=0 and a!=0:
            return a/b
        else:
            return "Error: Division por cero"""
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
        else:
            operador=int(operador)
    except ValueError:
        print("Error el operador es incorrecto Intente de nuevo.")
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
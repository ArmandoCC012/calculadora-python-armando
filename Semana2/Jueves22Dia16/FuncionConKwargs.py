#Crea una funcion que reciba datos de una persona (**kwargs) y los imprima en formato
# en formato bonito 
def MenuDeComedor(**valores):
    for c,v in valores.items():
          print(f"Nombre:{c},Caracteristica:{v}")
print("Ingresa varios atributos.")
diccio={}
while True:
    atributos=input("Nombre?:")
    atributos2=input("Caracteristica?:")
    diccio[atributos]=atributos2
    decision=input("Salir? X/x")
    if decision == 'x' or decision == 'X':
         break
print(f"Tus atributos son:")
MenuDeComedor(**diccio)



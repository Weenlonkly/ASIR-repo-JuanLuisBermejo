#Pide al usuario un número del 1 al 7 y muestra el día de la semana correspondiente:

#1: Lunes
#2: Martes
#...
#7: Domingo
#Si el número no está entre 1 y 7, imprime:
#"Número fuera de rango."

dia = int(input("Dame un numero del 1 al 7 y te dire el dia de la semana correspondiente: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("Número fuera de rango.")

#Pide al usuario un número. Si el número está entre 1 y 100 (inclusive), imprime:
#"El número está dentro del rango."
#Si no, imprime:
#"El número está fuera del rango."

numero = int(input("Introduce un número: "))

if numero >= 1  and numero <= 100:
    print("El número está dentro del rango.")
else:
    print("El número está fuera del rango.")

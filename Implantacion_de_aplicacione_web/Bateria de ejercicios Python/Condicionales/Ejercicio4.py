#Pide al usuario dos números. Usa condicionales para imprimir:

#"El primer número es mayor que el segundo."
#"El segundo número es mayor que el primero."
#"Ambos números son iguales."

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))

if num1 > num2:
    print("El primer número es mayor que el segundo.")
elif num2 > num1:
    print("El segundo número es mayor que el primero.")
else:
    print("Ambos números son iguales.")

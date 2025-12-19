#Declara una variable con un número cualquiera. Si el número es positivo, imprime:
#"El número es positivo."
#Si el número es negativo, imprime:
#"El número es negativo."
#Si el número es 0, imprime:
#"El número es cero."

numero = int(input("Dame un numero: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

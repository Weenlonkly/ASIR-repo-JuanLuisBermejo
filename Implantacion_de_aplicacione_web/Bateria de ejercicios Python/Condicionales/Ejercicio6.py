#Pide al usuario una letra. Si la letra es una vocal (a, e, i, o, u), imprime:
#"Es una vocal."
#Si no, imprime:
#"No es una vocal."

letra = input("Dame una letra: ").lower()

if letra in "aeiou":
    print("Es una vocal.")
else:
    print("No es una vocal.")

#Pide al usuario una contraseña y verifica si es igual a "secreto123". Si es correcta, imprime:
#"Acceso concedido."
#Si no, imprime:
#"Contraseña incorrecta."

password = input("Introduce la contraseña: ")

if password == "secreto123":
    print("Acceso concedido.")
else:
    print("Contraseña incorrecta.")

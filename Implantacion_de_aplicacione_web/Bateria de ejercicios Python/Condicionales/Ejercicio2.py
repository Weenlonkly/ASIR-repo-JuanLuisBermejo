#Pide al usuario su edad. Si tiene 18 años o más, imprime:
#"Eres mayor de edad."
#Si tiene menos de 18, imprime:
#"Eres menor de edad."

edad = int(input("Escribe tu edad: "))

if edad < 0:
    print("Ah vale no has nacido, bien.")
elif edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")


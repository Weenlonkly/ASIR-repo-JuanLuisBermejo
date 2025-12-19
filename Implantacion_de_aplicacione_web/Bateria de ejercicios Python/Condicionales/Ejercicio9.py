#Pide al usuario una temperatura en grados Celsius. Si la temperatura es:

#Mayor o igual a 30: imprime "Hace calor."
#Entre 10 y 29: imprime "El clima es templado."
#Menor a 10: imprime "Hace frío."

temp = float(input("Introduce la temperatura en ºC: "))

if temp >= 30:
    print("Hace calor.")
elif temp > 10 and temp <= 29:
    print("El clima es templado.")
else:
    print("Hace frío.")

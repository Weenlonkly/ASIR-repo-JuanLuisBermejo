#Pide al usuario el precio de un producto. Si el precio es mayor a 1000, aplica un descuento del 10% y muestra el precio final. Si no, muestra el precio sin descuento.

precio = int(input("Introduce el precio del producto: "))

if precio > 1000:
    print ("Hay un descuento del 10%")
    precio_final = precio * 0.9
    print ("El precio con descuento:", precio_final)
else:
    print ("No hay un descuentos.")
    print ("El precio se queda igual:", precio)

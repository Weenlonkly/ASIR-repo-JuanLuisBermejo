from pymongo import MongoClient
from prettytable import PrettyTable

def mostrar_coches():
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["bdcoches"]
    coleccion = db["coches"]

    coches = list(coleccion.find())

    if not coches:
        print("⚠️ No hay coches registrados.")
        return

    tabla = PrettyTable()
    tabla.field_names = ["Marca", "Modelo", "Color", "KM", "Precio"]

    for coche in coches:
        tabla.add_row([coche["marca"], coche["modelo"], coche["color"], coche["km"], coche["precio"]])

    print(tabla)

if __name__ == "__main__":
    mostrar_coches()

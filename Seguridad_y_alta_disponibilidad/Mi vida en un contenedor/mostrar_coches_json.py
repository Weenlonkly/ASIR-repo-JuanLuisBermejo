import mysql.connector
import json
from mysql.connector import Error

def cargar_configuracion():
    with open("config.json", "r") as archivo:
        return json.load(archivo)

def mostrar_coches():
    try:
        config = cargar_configuracion()

        conexion = mysql.connector.connect(
            host=config["host"],
            port=config["port"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )

        if conexion.is_connected():
            print("\n✅ CONEXIÓN EXITOSA A MySQL\n")

            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM vehiculos")
            resultados = cursor.fetchall()

            print("╔════╦════════════╦════════════╦════════╦════════╦══════════╗")
            print("║ ID ║ Marca      ║ Modelo     ║ Color  ║ KM     ║ Precio   ║")
            print("╠════╬════════════╬════════════╬════════╬════════╬══════════╣")

            for fila in resultados:
                id, marca, modelo, color, km, precio = fila
                print(f"║ {id:<2} ║ {marca:<10} ║ {modelo:<10} ║ {color:<6} ║ {km:<6} ║ ${precio:<8} ║")

            print("╚════╩════════════╩════════════╩════════╩════════╩══════════╝")

    except FileNotFoundError:
        print("❌ No se encontró el archivo config.json")
    except Error as e:
        print("❌ Error de conexión:", e)
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("\n🔌 Conexión cerrada correctamente.")

if __name__ == "__main__":
    mostrar_coches()

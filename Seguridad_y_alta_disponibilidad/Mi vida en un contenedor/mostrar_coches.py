import mysql.connector
from mysql.connector import Error

def mostrar_coches():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port=3307,
            user="root",
            password="Abcd1234",
            database="bdcoches"
        )

        if conexion.is_connected():
            print("\n✅ CONEXIÓN EXITOSA A MySQL\n")

            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM vehiculos")
            resultados = cursor.fetchall()

            if len(resultados) == 0:
                print("⚠️ No hay coches registrados.")
                return

            print("╔════╦════════════╦════════════╦════════╦════════╦══════════╗")
            print("║ ID ║ Marca      ║ Modelo     ║ Color  ║  KM    ║ Precio   ║")
            print("╠════╬════════════╬════════════╬════════╬════════╬══════════╣")

            for fila in resultados:
                id, marca, modelo, color, km, precio = fila
                print(f"║ {id:<2} ║ {marca:<10} ║ {modelo:<10} ║ {color:<6} ║ {km:<6} ║ ${precio:<8} ║")

            print("╚════╩════════════╩════════════╩════════╩════════╩══════════╝")

    except Error as e:
        print("❌ Error al conectar a MySQL:", e)

    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("\n🔌 Conexión cerrada correctamente.")

if __name__ == "__main__":
    mostrar_coches()

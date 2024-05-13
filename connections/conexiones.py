import pymysql
# Conexión a la base de datos
def connect_to_database():
    return pymysql.connect(host='localhost', user='root', passwd='root', db='usuarios')


# Función para filtrar y sumar
#corregir dependencias

def filtrar_y_sumar(id, CUENTA):
    conexion = connect_to_database()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT SUM(cantidad) FROM transacciones WHERE id = %s AND CUENTA = %s", (id, CUENTA))
            resultado = cursor.fetchone()[0]
            if resultado is None:
                print("No hay datos para este usuario y cuenta.")
            else:
                print(f"La suma total de la columna 'cantidad' para el usuario con id {id} y CUENTA {CUENTA} es: {resultado}")
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        conexion.close()
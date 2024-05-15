import pymysql

# Conexión a la base de datos
def connect_to_database():
    return pymysql.connect(host='localhost', user='root', passwd='root', db='usuarios')

def cantidad_por_cuenta(id, cuenta):
    conexion = connect_to_database()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT SUM(cantidad) FROM finanzas_user WHERE ID = %s AND CUENTA = %s", (id, cuenta))
            resultado = cursor.fetchone()[0]
            if resultado is None:
               return "$0.0"
            else:
               x=str(resultado)
               return "$"+x
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        conexion.close()

def total(id):
    conexion = connect_to_database()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT SUM(cantidad) FROM finanzas_user WHERE ID = %s ", (id))
            resultado = cursor.fetchone()[0]
            if resultado is None:
               return "$0.0"
            else:
               x=str(resultado)
               return "$"+x
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        conexion.close()


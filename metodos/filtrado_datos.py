import pymysql
import pandas as pd
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
               return "$"+resultado
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        conexion.close()

def datos_tabla(id):
    conexion=connect_to_database()
    cursor=conexion.cursor()
    try:
      cursor.execute("SELECT * FROM finanzas_user WHERE ID = %s",(id,))
      datos=cursor.fetchall()
      return datos
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        conexion.close()


import pymysql

# Conexión a la base de datos
def connect_to_database():
    return pymysql.connect(host='localhost', user='root', passwd='root', db='usuarios')

def cantidad_por_cuenta(id, cuenta):
    conexion = connect_to_database()  # Asegúrate de tener la función connect_to_database() definida
    cursor=conexion.cursor()
    cursor.execute("SELECT CANTIDAD FROM `finanzas_user` WHERE ID=%s AND CUENTA=%s", (id, cuenta))
    resultado = cursor.fetchall()
    if not resultado:
     return "$0.0"
    else:
     suma_total = sum(row[0] for row in resultado)
     return f"${suma_total:.2f}"
     conexion.close()

def total(id):
    conexion = connect_to_database()  # Asegúrate de tener la función connect_to_database() definida
    cursor=conexion.cursor()
    cursor.execute("SELECT CANTIDAD FROM `finanzas_user` WHERE ID=%s", (id))
    resultado = cursor.fetchall()
    if not resultado:
        return "$0.0"
    else:
        suma_total = sum(row[0] for row in resultado)
        return f"${suma_total:.2f}"
    

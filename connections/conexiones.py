import pymysql
# Conexión a la base de datos
def connect_to_database():
    return pymysql.connect(host='localhost', user='root', passwd='root', db='usuarios')

# Función para verificar credenciales de usuario y obtener su ID
def verificacion_existe(Id, password):
    conexion = connect_to_database()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT ID FROM users_passwords WHERE ID = %s AND PASSWORD = %s", (Id, password))
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]  # Devuelve el ID del usuario si se encuentra
            else:
                print("Usuario no encontrado.")
                return None
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        conexion.close()

# Función para filtrar y sumar
def filtrar_y_sumar(ID, cuenta):
    conexion = connect_to_database()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT SUM(cantidad) FROM transacciones WHERE id_usuario = %s AND cuenta = %s", (ID, cuenta))
            resultado = cursor.fetchone()[0]
            if resultado is None:
                print("No hay datos para este usuario y cuenta.")
            else:
                print(f"La suma total de la columna 'cantidad' para el usuario con ID {ID} y cuenta {cuenta} es: {resultado}")
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        conexion.close()

# Función para manejar la autenticación de usuario
def credenciales_usuario():
    user_id = int(usuario.get()) # type: ignore
    user_password = contraseña.get() # type: ignore
    user_id = verificacion_existe(user_id, user_password)
    if user_id:
        cuenta = cuenta_entry.get() # type: ignore
        filtrar_y_sumar(user_id, cuenta)
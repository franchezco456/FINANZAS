#intalar pymysql
import pymysql
def verificacion_existe(Id,password):
 #conexion a la base de datos
 conexionUsuarios= pymysql.connect(host='localhost', user = 'root', passwd='root', db='usuarios')
 #se crea un cur con la instancia de la conexion para hacer consultas
 cur=conexionUsuarios.cursor()
 #buscamos en las columnas id y password de la tabla users_passwords
 cur.execute("select ID, PASSWORD from users_passwords")
 #imprimimos los datos 
 for ID, PASSWORD in cur.fetchall():
  if(ID==Id and PASSWORD==password):
   print("true")
 conexionUsuarios.close()

def crear_Usuario(id_usuario, password):
    # Establecer conexión con la base de datos
    conexion = pymysql.connect(host='localhost', user='root', passwd='root', db='usuarios')
    cursor = conexion.cursor()
    
    # Crear nuevo usuario
    try:
        # Preparar la consulta SQL para insertar un nuevo usuario
        sql = "INSERT INTO users_passwords (ID, PASSWORD) VALUES (%s, %s)"
        # Ejecutar la consulta SQL
        cursor.execute(sql, (id_usuario, password))
        # Confirmar la transacción
        conexion.commit()
        print("Usuario agregado exitosamente.")
    except pymysql.Error as e:
        # Revertir en caso de error
        conexion.rollback()
        print(f"Error al agregar el usuario: {e}")
    finally:
        # Cerrar la conexión
        cursor.close()
        conexion.close()

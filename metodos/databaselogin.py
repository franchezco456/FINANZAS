#intalar pymysql
import pymysql
import subprocess
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
    subprocess.Popen(["python", "wallet.py"])
    UISS(Id)
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

def UISS(numero):
  nombre_archivo = "mi_archivo.txt"
    # Guardar el ultimo id en el archivo
  with open(nombre_archivo, "w") as archivo:
        archivo.write(str(numero))

def leer_desde_archivo():
    # Nombre del archivo
    nombre_archivo = "mi_archivo.txt"

    try:
        # Leer el contenido del archivo
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            numero_leido = int(contenido)
            return numero_leido
    except FileNotFoundError:
        print("El archivo no existe o no se puede leer.")
        return None



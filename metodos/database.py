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
    print(ID , " | " , PASSWORD)
 #se cierra la conexion a la base de datos
 conexionUsuarios.close()

def crear_Usuario():
  pass



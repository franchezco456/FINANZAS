import pymysql
import datetime
def ingreso(id,categoria,cantidad,cuenta):
     ahora=datetime.datetime.now()
     fecha=(ahora.strftime(("%Y/%m/%d")))
      # Establecer conexión con la base de datos
     conexion = pymysql.connect(host='localhost', user='root', passwd='root', db='usuarios')
     cursor = conexion.cursor()
      # Crear nuevo usuario
     try:
         # Preparar la consulta SQL para insertar un nuevo usuario
         sql = "INSERT INTO finanzas_user (ID, CATEGORIA, FECHA, CANTIDAD,CUENTA) VALUES (%s, %s, %s, %s,%s)"
        # Ejecutar la consulta SQL
         cursor.execute(sql, (id, categoria,fecha,cantidad,cuenta))
         # Confirmar la transacción
         conexion.commit()
         print("transaccion agregada exitosamente")
     except pymysql.Error as e:
         # Revertir en caso de error
         conexion.rollback()
         print(f"Error al agregar la transaccion: {e}")
     finally:
         # Cerrar la conexión
         cursor.close()
         conexion.close()
#SELECT * FROM `finanzas_user`
def egreso(id,categoria,cantidad,cuenta):
     ahora=datetime.datetime.now()
     fecha=(ahora.strftime(("%Y/%m/%d")))
      # Establecer conexión con la base de datos
     if(cantidad>0):
         cantidad=cantidad*-1
     conexion = pymysql.connect(host='localhost', user='root', passwd='root', db='usuarios')
     cursor = conexion.cursor()
      # Crear nuevo usuario
     try:
         # Preparar la consulta SQL para insertar un nuevo usuario
         sql = "INSERT INTO finanzas_user (ID, CATEGORIA, FECHA, CANTIDAD,CUENTA) VALUES (%s, %s, %s, %s,%s)"
        # Ejecutar la consulta SQL
         cursor.execute(sql, (id, categoria,fecha,cantidad,cuenta))
         # Confirmar la transacción
         conexion.commit()
         print("transaccion agregada exitosamente")
     except pymysql.Error as e:
         # Revertir en caso de error
         conexion.rollback()
         print(f"Error al agregar la transaccion: {e}")
     finally:
         # Cerrar la conexión
         cursor.close()
         conexion.close()




    
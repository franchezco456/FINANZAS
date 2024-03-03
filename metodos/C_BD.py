#intalar pymysql
import pymysql
conexionUsuarios= pymysql.connect(host='localhost', user = 'root', passwd='root', db='usuarios')
cur=conexionUsuarios.cursor()

cur.execute("select ID, PASSWORD from users_passwords")
for ID, PASSWORD in cur.fetchall():
    print(ID , " | " , PASSWORD)
   
conexionUsuarios.close()



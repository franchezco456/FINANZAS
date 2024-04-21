from customtkinter import CTk, CTkFrame

from tkinter import Tk, PhotoImage

from metodos.database import verificacion_existe
#Variables:
c_negro = '#010101'


def credenciales_usuario():
     user_id=int(usuario.get())
     print(user_id)
     user_password=contraseña.get()
     print(user_password)
     verificacion_existe(user_id,user_password)




ventana = Tk()
#Colocar titulo
ventana.title("INICIAR DE SESION")
#Tamaño
ventana.geometry('500x600+350+20')
#Tamaño minimo
ventana.minsize(480,500)
#Evitar ajustar el tamaño manualmente
ventana.resizable(width=False, height=False)
#darle un color
ventana.config(bg= c_negro)

#Iconito 
icono = PhotoImage (file='pictures/icono.png')

#Mostrar icono
ventana.iconphoto(True, icono)
ventana.mainloop()

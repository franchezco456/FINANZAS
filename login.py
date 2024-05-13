from customtkinter import CTk, CTkFrame, CTkEntry, CTkButton, CTkLabel
from tkinter import Tk, PhotoImage
from metodos.databaselogin import verificacion_existe, crear_Usuario
#Variables:
c_negro = '#010101'
c_azul  = '#3B83BD'
c_morado= '#2cb67d'

def credenciales_usuario():

     user_id=int(usuario.get())
     print(user_id)
     user_password=contraseña.get()
     print(user_password)
     verificacion_existe(user_id,user_password)

def new_user():
     user_id=int(usuario.get())
     print(user_id)
     user_password=contraseña.get()
     print(user_password)
     crear_Usuario(user_id,user_password)




ventana = Tk()
#CARACTERISTICAS DE LA VENTANA_
#Colocar titulo
ventana.title("INICIO DE SESION")
#Tamaño
ventana.geometry('500x600+350+20')
#Tamaño minimo
ventana.minsize(480,500)
#Evitar ajustar el tamaño manualmente
ventana.resizable(width=False, height=False)
#darle un color
ventana.config(bg= c_negro)

#Imagenes usadas: 
#Iconito 
icono = PhotoImage (file='pictures/icono.png')
icono2 =  PhotoImage (file='pictures/icono_2.png')

#Botones y otras cosas
ventana.columnconfigure(0,weight=1)
ventana.rowconfigure(0, weight=1)

#Colocar un icono a la ventana
CTkLabel(ventana, text='', image=icono2).grid(columnspan =2, row=0)

#Usuario y contraseña_
#Se crea el usuario y se establecen los parametros como el color tamaño etc que tendra la entrda
usuario = CTkEntry(ventana, placeholder_text = 'Correo Electronico', 
                   border_color=c_azul, fg_color= c_negro, width=220, height=40)
#Usando .grid hace que se muestren en la interfaz grafica
usuario.grid(columnspan =2, row=1, padx=4, pady=4)
contraseña = CTkEntry(ventana, placeholder_text = 'Contraseña', 
                      border_color=c_azul, fg_color= c_negro, width=220, height=40)
contraseña.grid(columnspan =2, row=2, padx=4, pady=4)





#Boton iniciar sesion
bt_iniciar= CTkButton(ventana, border_color=c_azul, fg_color= c_negro, 
                      hover_color=c_morado, corner_radius=12, border_width=2 ,text='Iniciar Sesion', height=40,command=credenciales_usuario)
bt_iniciar.grid(columnspan=1, row= 4, pady=4, padx=4)

#Boton registrarse
bt_Registrar= CTkButton(ventana, border_color=c_azul, fg_color= c_negro, 
                      hover_color=c_morado, corner_radius=12, border_width=2 ,text='Registrarse', height=40,command=new_user)
bt_Registrar.grid(columnspan=2, row= 5, pady=4, padx=4)





#Mostrar icono
ventana.iconphoto(True, icono)
ventana.mainloop()

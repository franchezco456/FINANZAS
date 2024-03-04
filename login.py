from customtkinter import *
#Crear la ventana
app = CTk() 
def verificacion_existe():
     user_id=usuario.get()
     user_password=contraseña.get()
     



#Colocar titulo
app.title("INICIO DE SESION")
#Crear un cuadro dentro de la ventana
frame = CTkFrame(master=app, fg_color="#000000", border_color="#FFCC70", border_width=2)
frame.pack(expand=True)
#Ingreso botones y titulo
titulo= CTkLabel(master=frame, text="INICIO DE SESION", text_color="#801B1B")
usuario= CTkEntry(master=frame, placeholder_text="Ingrese usuario")
contraseña= CTkEntry(master=frame, placeholder_text="Ingrese Contraseña")
ingresar= CTkButton(master=frame, text="Ingresar",command=verificacion_existe)
registrar= CTkButton(master=frame, text="Registrarse")

#Colocar los botones
titulo.pack(anchor="s", expand=True, pady=10, padx=30)
usuario.pack(anchor="s", expand=True, pady =10, padx=30)
contraseña.pack(anchor="s", expand=True, pady =10, padx=30)
ingresar.pack(anchor="n", expand=True, padx=30, pady=20)
registrar.pack(anchor="n", expand=True, padx=30, pady=20)
app.mainloop()

#img= Image.open("mensaje.jpg")
#image=CTkImage(dark_image=img, light_image=img))
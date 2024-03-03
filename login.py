from customtkinter import *
#Crear la ventana
app = CTk() 
#Colocar titulo
app.title("INICIO DE SESION")
#Crear un cuadro dentro de la ventana
frame = CTkFrame(master=app, fg_color="#000000", border_color="#FFCC70", border_width=2)
frame.pack(expand=True)

#Ingreso botones y titulo
Titulo= CTkLabel(master=frame, text="INICIO DE SESION", text_color="#801B1B")
Usuario= CTkEntry(master=frame, placeholder_text="Ingrese usuario")
Contraseña= CTkEntry(master=frame, placeholder_text="Ingrese Contraseña")
Ingresar= CTkButton(master=frame, text="Ingresar")
Registrar= CTkButton(master=frame, text="Registrarse")

#Colocar los botones
Titulo.pack(anchor="s", expand=True, pady=10, padx=30)
Usuario.pack(anchor="s", expand=True, pady =10, padx=30)
Contraseña.pack(anchor="s", expand=True, pady =10, padx=30)
Ingresar.pack(anchor="n", expand=True, padx=30, pady=20)
Registrar.pack(anchor="n", expand=True, padx=30, pady=20)
app.mainloop()

#img= Image.open("mensaje.jpg")
#image=CTkImage(dark_image=img, light_image=img))
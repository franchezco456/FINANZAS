from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkEntry
from tkinter import *
from tkinter import Tk, PhotoImage, ttk
#Lista de Variables
c_negro = '#010101'
c_azul  = '#3B83BD'
c_morado= '#56145b'
c_verde = '#008000'
c_blanco = '#FFFFFF'

#Crear ventanas y configuracion
enter= Tk()
enter.title("Ingreso de Ingresos")
enter.geometry('700x500+350+20')
enter.minsize(680,700)
enter.resizable(width=False, height=False)
enter.config(bg= c_negro)
#Imagenes
icono = PhotoImage (file='pictures/icono.png')
icono_back = PhotoImage (file='pictures/back.png')
icono_water= PhotoImage (file='pictures/water.png')
enter.iconphoto(True, icono)


#Frame/ventana
frame_principal=CTkFrame(enter, fg_color= c_negro, width=680, height=670)
frame_principal.grid(columnspan=1,row=0, sticky='nsew',padx=10, pady=20)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)



frame_superior=CTkFrame(frame_principal,corner_radius=12,border_width=2,border_color=c_azul, fg_color= c_negro, width=670, height=500)
frame_superior.place(x=1, y=1)
frame_superior.grid_rowconfigure(1, weight=1)
frame_superior.grid_columnconfigure(1, weight=1) 

categorias = ["Comidas","Compras","Viviendas","Transporte","Vehiculos","Vida y Entretenimineto","Comunicaciones","Gastos financieros",
              "Inversiones","Ingresos","Otros..."]
cb_categorias = ttk.Combobox(frame_superior, values=categorias,state='readonly',font=("Arial",12))
cb_categorias.place(x=130, y=50)

cuentas= ["Efectivo","Banco","Ahorros"]
cb_cuentas=ttk.Combobox(frame_superior, values=cuentas,state='readonly',font=("Arial",12))
cb_cuentas.place(x=130, y=110)

CTkLabel(frame_superior, corner_radius=12,bg_color=c_azul, text='CATEGORIAS', font=("Arial",12), text_color=c_blanco).place(x=10, y=50)
CTkLabel(frame_superior, corner_radius=12,bg_color=c_azul, text='CUENTA', font=("Arial",12),width=100, text_color=c_blanco).place(x=10, y=110)

frame_inferior=CTkFrame(frame_principal,corner_radius=12,border_width=2,border_color=c_azul, fg_color=  c_negro,width=670, height=150)
frame_inferior.place(x=1, y=510)

CTkLabel(frame_inferior, corner_radius=12,bg_color=c_azul, text='SALDO ACTUAL', font=("Arial",12),width=125, text_color=c_blanco).place(x=10, y=80)
saldo=CTkLabel(frame_inferior,text='$0000000',corner_radius=12,fg_color=c_azul, font=("Arial",18), text_color=c_blanco).place(x=150, y=80)

CTkLabel(frame_inferior, corner_radius=12,bg_color=c_azul, text='USUARIO ACTUAL', font=("Arial",12), text_color=c_blanco).place(x=10, y=20)
usuario=CTkLabel(frame_inferior,text='Fulanito@gmail.com',corner_radius=12,fg_color=c_azul, font=("Arial",18), text_color=c_blanco).place(x=150, y=20)
#Boton
ingreso = CTkEntry(frame_superior,font=("Arial",18),placeholder_text = 'Ingrese los ingresos aqui',
                   border_color=c_azul, fg_color= c_negro, width=250, height=30)
ingreso.place(x=20, y=200)

bt_ingresar= CTkButton(frame_superior,text="ACEPTAR", font=("Arial",20),text_color=c_azul, border_color=c_azul, fg_color= c_negro, 
                      hover_color=c_morado, corner_radius=12, border_width=2 , height=40)
bt_ingresar.place(x=50, y=250)






bt_volver= CTkButton(frame_principal,image=icono_back,text='',border_color=c_azul, fg_color=c_negro,
                      hover_color=c_verde, corner_radius=12, border_width=2 ,height=5, width=5)
bt_volver.place(x=1, y=1)




enter.mainloop()
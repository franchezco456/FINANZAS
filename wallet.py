from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel
from tkinter import *
from tkinter import Tk, PhotoImage, ttk
import subprocess
from metodos.filtrado_datos import cantidad_por_cuenta
from metodos.databaselogin import leer_desde_archivo

#Lista de Variables
c_negro = '#010101'
c_azul  = '#3B83BD'
c_morado= '#56145b'
c_verde = '#008000'
c_blanco = '#FFFFFF'



#Procesos
def obtener_id():
    x=leer_desde_archivo()
    return x
def open_ingreso():
    subprocess.Popen(["python","enter.py"])
id=obtener_id()
def cantidad_labels(id,cuenta):
    a= cantidad_por_cuenta(id,cuenta)
    return a



efectivo=cantidad_labels(id,"Efectivo")
banco=cantidad_labels(id,"Banco" )
ahorros=cantidad_labels(id,"Ahorros")
#Crear ventanas 
ventana= Tk()
ventana.title("Administrador de Finanzas")
ventana.geometry('1000x700+350+20')
ventana.resizable(width=False, height=False)
icono = PhotoImage (file='pictures/icono.png')
fondo = PhotoImage (file='pictures/fondo.png')
ventana.iconphoto(True, icono)
ventana.config(bg= c_negro)

fondito = Label(ventana, image=fondo)
fondito.place(x=0, y=0, relwidth=1, relheight=1)

#Frame
frame_principal=CTkFrame(ventana, fg_color= c_negro, width=970, height=650)
frame_principal.grid(columnspan=1,row=0, sticky='nsew',padx=10, pady=20)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)
fondito = Label(frame_principal, image=fondo)
fondito.place(x=0, y=0, relwidth=1, relheight=1)
#Zona cuentas
#Frame de cuentas
c_frame=CTkFrame(frame_principal,corner_radius=12,border_width=2,border_color=c_azul, fg_color= c_negro, width=480, height=100)
c_frame.place(x=250, y=20)
CTkLabel(c_frame, text='CUENTA BANCARIA',bg_color=c_azul,  font=("Arial",12),width=125, text_color=c_blanco).grid(column=1, row=0,padx=10, pady=10)
c_bancaria=CTkLabel(c_frame, text=banco).grid(column=1, row=1,padx=10, pady=10)
CTkLabel(c_frame, text='CUENTA EFECTIVO',bg_color=c_azul,  font=("Arial",12),width=125, text_color=c_blanco).grid(column=2, row=0,padx=10, pady=10)
c_efectivo=CTkLabel(c_frame, text=efectivo).grid(column=2, row=1,padx=10, pady=10)
CTkLabel(c_frame, text='CUENTA AHORROS',bg_color=c_azul,  font=("Arial",12),width=125, text_color=c_blanco).grid(column=3, row=0,padx=10, pady=10)
c_ahorros=CTkLabel(c_frame, text=ahorros).grid(column=3, row=1, padx=10, pady=10)

#Zona Cuadro Historial
h_frame= CTkFrame(frame_principal, border_color=c_azul, fg_color= c_negro, border_width=2,width=500, height=350)
h_frame.place(x=230, y=150)




#Zona de botones


bt_ingresos= CTkButton(frame_principal, border_color=c_azul, fg_color= c_negro, 
                      hover_color=c_morado, corner_radius=12, border_width=2 ,text='INGRESAR INGRESOS', height=40, 
                      command=open_ingreso)
bt_ingresos.place(x=300,y=550)

bt_gastos= CTkButton(frame_principal, border_color=c_azul, fg_color= c_negro, 
                      hover_color=c_morado, corner_radius=12, border_width=2 ,text='INGRESAR GASTOS', height=40)
bt_gastos.place(x=500,y=550)







ventana.mainloop()
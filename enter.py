from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkEntry
from tkinter import *
from tkinter import Tk, PhotoImage, ttk
from metodos.databaselogin import leer_desde_archivo
from metodos.filtrado_datos import total
from metodos.ingresos_egresos import ingreso,egreso
#Lista de Variables
c_negro = '#010101'
c_azul  = '#3B83BD'
c_morado= '#56145b'
c_verde = '#008000'
c_blanco= '#FFFFFF'
c_gris  = '#3B3D3E'
def obtener_id():
    x=leer_desde_archivo()
    return x

id=obtener_id()

def cantidad(x):
    waos=total(x)
    return waos

gg=cantidad(id)
#Crear ventanas y configuracion
ventana= Tk()
ventana.title("Ingreso de Ingresos")
ventana.geometry('700x500+350+20')
ventana.minsize(680,700)
ventana.resizable(width=False, height=False)
ventana.config(bg= c_negro)
#Imagenes
icono_back = PhotoImage (file='pictures/back.png')
icono = PhotoImage (file='pictures/icono.png')
fondo = PhotoImage (file='pictures/fondo.png')
ventana.iconphoto(True, icono)
ventana.config(bg= c_negro)
fondito = Label(ventana, image=fondo)
fondito.place(x=0, y=0, relwidth=1, relheight=1)

#Frame/ventana
frame_principal=CTkFrame(ventana, fg_color= c_negro, width=680, height=670)
frame_principal.grid(columnspan=1,row=0, sticky='nsew',padx=10, pady=20)
frame_principal.grid_rowconfigure(0, weight=1)
frame_principal.grid_columnconfigure(0, weight=1)
fondito = Label(frame_principal, image=fondo)
fondito.place(x=0, y=0, relwidth=1, relheight=1)

#Zona de Frames
#Frame superior
frame_superior=CTkFrame(frame_principal,corner_radius=12,border_width=2,border_color=c_azul, fg_color= c_negro, width=670, height=500)
frame_superior.place(x=1, y=1)
frame_superior.grid_rowconfigure(1, weight=1)
frame_superior.grid_columnconfigure(1, weight=1) 
#Opcion categorias
categorias = ["Comidas","Compras","Viviendas","Transporte","Vehiculos","Vida y Entretenimineto","Comunicaciones","Gastos financieros",
              "Inversiones","Ingresos","Otros..."]
cb_categorias = ttk.Combobox(frame_superior, values=categorias,state='readonly',font=("Arial",12))
cb_categorias.place(x=320, y=50)

cuentas= ["Efectivo","Banco","Ahorros"]
cb_cuentas=ttk.Combobox(frame_superior, values=cuentas,state='readonly',font=("Arial",12))
cb_cuentas.place(x=320, y=110)

CTkLabel(frame_superior, corner_radius=12,bg_color=c_azul, text='CATEGORIAS', font=("Arial",12), text_color=c_blanco).place(x=550, y=50)
CTkLabel(frame_superior, corner_radius=12,bg_color=c_azul, text='CUENTA', font=("Arial",12),width=100, text_color=c_blanco).place(x=550, y=110)



#Frame inferior
frame_inferior=CTkFrame(frame_principal,corner_radius=12,border_width=2,border_color=c_azul, fg_color=  c_negro,width=670, height=150)
frame_inferior.place(x=1, y=510)

CTkLabel(frame_inferior, corner_radius=12,bg_color=c_azul, text='SALDO ACTUAL', font=("Arial",12),width=125, text_color=c_blanco).place(x=10, y=80)
saldo=CTkLabel(frame_inferior,text=gg,corner_radius=12,fg_color=c_azul, font=("Arial",18), text_color=c_blanco).place(x=150, y=80)

CTkLabel(frame_inferior, corner_radius=12,bg_color=c_azul, text='USUARIO ACTUAL', font=("Arial",12), text_color=c_blanco).place(x=10, y=20)
usuario=CTkLabel(frame_inferior,font=("Arial",18),text= id,
                    fg_color= c_azul, width=250, height=30).place(x=150, y=20)



#BOTONES Y ENTRADAS
aceptar = CTkEntry(frame_superior,font=("Arial",18),placeholder_text= '0',
                   border_color=c_azul, fg_color= c_negro, width=250, height=30)
aceptar.place(x=350, y=200)

def subir():
    categoria=cb_categorias.get()
    cuenta=cb_cuentas.get()
    canti=float(aceptar.get())
    ingreso(id,categoria,canti,cuenta)

bt_ingresar= CTkButton(frame_superior,text="ACEPTAR", font=("Arial",20),text_color=c_azul, border_color=c_azul, fg_color= c_negro, 
                      hover_color=c_morado, corner_radius=12, border_width=2 , height=40,command=subir)
bt_ingresar.place(x=400, y=250)





frame_inst=CTkFrame(frame_superior,corner_radius=12,border_width=2,border_color=c_azul, fg_color=  c_gris,width=200, height=400)
frame_inst.place(x=40, y=20)
CTkLabel(frame_inst, corner_radius=12,bg_color=c_azul, text='INSTRUCCIONES PARA TONTOS', font=("Arial",12), text_color=c_blanco).grid(column=1,row=0)
CTkLabel(frame_inst, corner_radius=12,text='1.Seleccionar una Categoria', font=("Arial",12), text_color=c_blanco).grid(column=1,row=1)
CTkLabel(frame_inst, corner_radius=12,text='2.Seleccionar una cuenta', font=("Arial",12), text_color=c_blanco).grid(column=1,row=2)
CTkLabel(frame_inst, corner_radius=12, text='3.Ingresar los ingresos', font=("Arial",12), text_color=c_blanco).grid(column=1,row=3)
CTkLabel(frame_inst, corner_radius=12, text='4.Presionar el Boton Aceptar', font=("Arial",12), text_color=c_blanco).grid(column=1,row=4)
CTkLabel(frame_inst, corner_radius=12, text='5.Presionar el Boton en la\nEsquina superior izquierda\nsi desea volver', font=("Arial",12),
          text_color=c_blanco).grid(column=1,row=4, pady=10)

bt_volver= CTkButton(frame_principal,image=icono_back,text='',border_color=c_azul, fg_color=c_negro,
                      hover_color=c_verde, corner_radius=12, border_width=2 ,height=5, width=5)
bt_volver.place(x=1, y=1)




ventana.mainloop()
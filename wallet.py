from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel
from tkinter import *
from tkinter import Tk, PhotoImage, ttk
import subprocess

#Lista de Variables
c_negro = '#010101'
c_azul  = '#3B83BD'
c_morado= '#2cb67d'
c_verde = '#008000'
def open_ingreso():
    subprocess.Popen(["python","enter.py"])
#Crear ventanas 
aplicacion= Tk()



#Ajustes de la ventana:
aplicacion.title("Administrador de Finanzas")
aplicacion.geometry('1000x700+350+20')
aplicacion.minsize(680,700)
aplicacion.resizable(width=False, height=False)
icono = PhotoImage (file='pictures/icono.png')
fondo = PhotoImage (file='pictures/fondo.png')
aplicacion.iconphoto(True, icono)
aplicacion.config(bg= c_negro)



background_label = Label(aplicacion, image=fondo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
#>ZONA DE CUENTAS: 

#(c_frame) son cuadros ligados a la ventana que sirven como medio para contener ciertas posiciones 
#Seguido sigue un CTKLabel el cual es la frase que estara dentro del cuadro
#Por ultimo la variable (c_bancaria/c_efectivo/c_ahorros) es con la que se puede modificar que es el $0000

c_frame1= CTkFrame(aplicacion, fg_color=c_negro)
c_frame1.grid(column=0,row=0, sticky='nsew',padx=30, pady=30)
background_label = CTkLabel(c_frame1, text='', image=fondo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
c_frameC= CTkFrame(c_frame1,corner_radius=12,border_width=2,border_color=c_azul, fg_color= c_negro)
c_frameC.grid(column=0,row=0, sticky='nsew',padx=30, pady=30)


c_frame2= CTkFrame(c_frameC, fg_color=c_negro,border_color=c_azul,width=60, height=300)
c_frame2.grid(column=0,row=0, sticky='nsew',padx=10, pady=10)
CTkLabel(c_frame2, text='CUENTA BANCARIA').grid(columnspan =1, row=0)
#Variable
c_bancaria=CTkLabel(c_frame2, text='$00000').grid(columnspan=1, row=1)


c_frame3= CTkFrame(c_frameC, fg_color=c_negro,width=60, height=300)
c_frame3.grid(column=1,row=0, sticky='nsew',padx=10, pady=10)
CTkLabel(c_frame3, text='CUENTA EFECTIVO').grid(columnspan =1, row=0)
#Variable
c_efectivo=CTkLabel(c_frame3, text='$00000').grid(columnspan=1, row=1)

c_frame4= CTkFrame(c_frameC, fg_color=c_negro,width=100, height=300)
c_frame4.grid(column=2,row=0, sticky='nsew',padx=10, pady=10)
CTkLabel(c_frame4, text='CUENTA AHORROS').grid(columnspan =1, row=0)
#Variable
c_ahorros=CTkLabel(c_frame4, text='$00000').grid(columnspan=1, row=1)
#///////////END OF CUENTAS ZONE

#>ZONA DE CUADROS

#CUADRO GRAFICA PASTEL
c_framep= CTkFrame(c_frame1, border_color=c_azul, fg_color= c_negro, border_width=2, width=200, height=300)
c_framep.grid(column=0,row=1, sticky='nsew',padx=30, pady=30)
#(Cuando vayan a colocar el cuadro tienen que indicar que estara en "c_framep" no en "aplicacion"(ventana principal) porque se lia todo)




#CUADRO HISTORIAL
c_frameh= CTkFrame(c_frame1, border_color=c_azul, fg_color= c_negro, border_width=2,width=400, height=300)
c_frameh.grid(column=1,row=1, sticky='nsew',padx=30, pady=30)
#(Cuando vayan a colocar el cuadro tienen que indicar que estara en "c_frameh" no en "aplicacion"(ventana principal) porque se lia todo)

historial= ttk.Treeview(c_frameh)
historial.insert("",END, text="ELEMENTO 1")
historial.place(x=10,y=10)

#///////////END OF ZONA DE CUADROS





aplicacion.columnconfigure(0,weight=1)
aplicacion.rowconfigure(0, weight=1)


#Incertar botones
c_frameb= CTkFrame(aplicacion, fg_color=c_negro,width=100, height=100)
c_frameb.grid(column=0,row=2, sticky='nsew',padx=30, pady=30)
background_label = Label(c_frameb, image=fondo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
bt_ingresos= CTkButton(c_frameb, border_color=c_azul, fg_color= c_negro, 
                      hover_color=c_morado, corner_radius=12, border_width=2 ,text='INGRESAR INGRESOS', height=40, command=open_ingreso)
bt_ingresos.grid(row=0, column=0, pady=12, padx=30)

bt_gastos= CTkButton(c_frameb, border_color=c_azul, fg_color= c_negro, 
                      hover_color=c_morado, corner_radius=12, border_width=2 ,text='INGRESAR GASTOS', height=40)
bt_gastos.grid(row=0, column=2, pady=4, padx=30)


aplicacion.mainloop()
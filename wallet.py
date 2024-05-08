from customtkinter import CTk, CTkFrame, CTkEntry, CTkButton, CTkLabel
from tkinter import Tk, PhotoImage
#Lista de Variables
c_negro = '#010101'
c_azul  = '#3B83BD'

#Crear ventanas 
aplicacion= Tk()



#Ajustes de la ventana:
aplicacion.title("Administrador de Finanzas")
aplicacion.geometry('700x700+350+20')
aplicacion.minsize(680,700)
aplicacion.resizable(width=False, height=False)
icono = PhotoImage (file='pictures/icono.png')
aplicacion.iconphoto(True, icono)
aplicacion.config(bg= c_negro)


frame1= CTkFrame(aplicacion, fg_color=c_azul)
frame1.grid(column=0,row=0, sticky='nsew',padx=30, pady=30)



aplicacion.columnconfigure(0,weight=1)
aplicacion.rowconfigure(0, weight=1)

aplicacion.mainloop()
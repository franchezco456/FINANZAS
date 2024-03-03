from customtkinter import *
from PIL import Image
app = CTk()
app.geometry=("800x600")
def boton_1_click():
    print("boton aceptar a sido presionado")
img= Image.open("mensaje.jpg")
label=CTkLabel(master=app, text="USUARIO: ", font=("Arial",20), text_color="#FFCC70")
label.place(relx=0.5, rely=0.5, anchor="e")
btn = CTkButton (master=app, text="Aceptar", corner_radius=32, fg_color="transparent"
btn = CTkButton (master=app, text="Aceptar", command=boton_1_click,corner_radius=32, fg_color="transparent",
 hover_color="#4158D0", border_color="#FFFF00", border_width=2, 
   image=CTkImage(dark_image=img, light_image=img))
btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()

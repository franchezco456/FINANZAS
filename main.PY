from customtkinter import *
from PIL import Image
app = CTk()
app.geometry=("800x600")
img= Image.open("mensaje.jpg")
btn = CTkButton (master=app, text="Aceptar", corner_radius=32, fg_color="transparent",
                 hover_color="#4158D0", border_color="#FFFF00", border_width=2, 
                 image=CTkImage(dark_image=img, light_image=img))
btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()

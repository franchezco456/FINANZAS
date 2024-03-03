from customtkinter import *

app = CTk()
app.geometry=("1200x1000")

btn = CTkButton (master=app, text="Aceptar", corner_radius=32, fg_color="#FF0000", 
                 hover_color="#0000ff")
btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()

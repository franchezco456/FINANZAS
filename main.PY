from customtkinter import *

app = CTk()
app.geometry=("800x600")

btn = CTkButton (master=app, text="Aceptar", corner_radius=32, fg_color="#FF0000",
                 hover_color="#4158D0")
btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()

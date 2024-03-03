from customtkinter import *

app = CTk()
app.geometry=("800x600")

btn = CTkButton (master=app, text="Aceptar")
btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()

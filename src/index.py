from tkinter import Tk, Label

window = Tk()
window.title("Budjetointisovellus")

label_welcome = Label(window, text="Terveuloa budjetointisovellukseen!")
label_login = Label(window, text="Kirjaudu: ")

label_welcome.grid(row=0, column=0)
label_login.grid(row=3, column=1)

window.mainloop()

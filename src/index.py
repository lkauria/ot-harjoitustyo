from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("Budjetointisovellus")
window.geometry("400x200")

def login():
    login_label = Label(window, text="Logiikka kirjautumiselle alkaa")
    login_label.grid(row=4, column=1)

label_welcome = Label(window, text="Terveuloa budjetointisovellukseen!")
button_login = Button(window, text="Kirjaudu", padx=50, pady=20, command=login, bg="#66cdaa")

entry_username = Entry(window, width=60)
entry_password = Entry(window, width=60)

entry_username.insert(0, "käyttäjänimesi ")
entry_password.insert(0, "salasanasi ")

label_welcome.grid(row=0, column=1)
button_login.grid(row=3, column=1)
entry_username.grid(row=1, column=1)
entry_password.grid(row=2, column=1)

window.mainloop()

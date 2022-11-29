from tkinter import Tk, Label, Button, Entry
from ui.ui import UI

def main():
    window = Tk()
    window.title("Budjetointisovellus")
    window.geometry("800x400")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()
from tkinter import Tk
from ui.ui import UI


def main():
    """This main starts the application and creates UI window.
    """
    window = Tk()
    window.title("Budjetointisovellus")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()

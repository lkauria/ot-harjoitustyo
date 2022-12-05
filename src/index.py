from tkinter import Tk
from ui.ui import UI
from repositories.user_repository import user_repository


def main():
    window = Tk()
    window.title("Budjetointisovellus")
    window.geometry("800x400")

    ui_view = UI(window)
    ui_view.start()

    print(user_repository.find_all())
    window.mainloop()

if __name__ == "__main__":
    main()

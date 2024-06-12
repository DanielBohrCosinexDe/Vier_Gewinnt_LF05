import ttkbootstrap as tb
#from ttkbootstrap import *
from view.menu import Menu


class App(tb.Window):
    def __init__(self):
        super().__init__(themename='superhero')


def main():
    app = App()
    menu = Menu(app)
    app.mainloop()


if __name__ == "__main__":
    main()

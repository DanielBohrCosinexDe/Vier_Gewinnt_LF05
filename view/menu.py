import ttkbootstrap as tb

class Menu(tb.Frame):
    def __init__(self, mainWindow):
        super().__init__(mainWindow, bootstyle = "primary",width=400,height=600)
        self.pack()

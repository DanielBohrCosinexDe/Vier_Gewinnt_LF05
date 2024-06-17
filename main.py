import ttkbootstrap as tb
from ttkbootstrap.constants import *
from dotenv import dotenv_values
from view.menu import Menu
from view.menu import Game


# Enviroment Variables
config = {
    **dotenv_values('.env')
}

class App(tb.Window):
    def __init__(self,title=config['TITLE'],size=(config['WIDTH'],config['HIGHT']),themename=config['THEME']):

        #main Window
        super().__init__(themename=themename)
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')

def main():
    
    app = App()
     #Frames or widgets
    menu = Menu(app)
    #game = Game(app)

    
        
    #run Window
    app.mainloop()

if __name__ == "__main__":
    main()
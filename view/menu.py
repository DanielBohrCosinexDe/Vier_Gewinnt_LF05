import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog
from dotenv import dotenv_values


## My Import
from model.ai import AI
from .game import Game
from model.piece import Piece
from model.player import Player

config = {
    **dotenv_values('.env')
}

class Menu(tb.Frame):
    def __init__(self,main_window:tb.Window):
        
        #init Frame
        super().__init__(main_window, padding=(30,10))
            
        # grid layout 
        self.rowconfigure((0,1,2,3), weight = 1)
        self.columnconfigure(0, weight = 1, uniform = 'a')
        
        #Player Info
        self.player1_name = tb.StringVar(value=config['PLAYER1_DEFAULT_NAME'])
        self.player2_name = tb.StringVar(value=config['PLAYER2_DEFAULT_NAME'])
        self.ai = False
        self.piece1= Piece(config['PLAYER1_DEFAULT_COLOR'])
        self.piece2= Piece(config['PLAYER2_DEFAULT_COLOR'])
        
        
        self.ai_strategy = tb.StringVar(value='Random')
        
        
        # Create Players Name Input
        self.create_form_entry(config['PLAYER1_DEFAULT_NAME'], self.player1_name,self.piece1).grid(row = 0)
        
        
        # toggle option for Ai
        toggle_button_ai_value = tb.IntVar(value=0)
        
        # Create Players Name Input
        player2_entry=self.create_form_entry(config['PLAYER2_DEFAULT_NAME'], self.player2_name,self.piece2)
        
        #create toggle ai button
        self.create_toggle_button(toggle_button_ai_value,player2_entry).grid(row=1,ipadx=72)
        
        # Create Players Name Input
        player2_entry.grid(row = 2)        
        
        
        # start game button
        button_start_game=tb.Button(self,text='Start Game',command=lambda: self.handel_click(main_window),bootstyle=PRIMARY)
        button_start_game.grid(row = 3)
        
        self.pack(fill=BOTH,expand=YES)
    
    def create_toggle_button(self,toggle_button_ai_value,player2_entry):
        toggle_button_ai_container = tb.Frame(self)
        
        ai_label = tb.Label(toggle_button_ai_container, text='Play against AI')
        ai_label.pack(side=LEFT , padx= 10)
        
        toggle_button_ai = tb.Checkbutton(toggle_button_ai_container,text='',bootstyle="primary-round-toggle",variable=toggle_button_ai_value,onvalue=1,offvalue=0,command=lambda: tg())
        toggle_button_ai.pack(side=LEFT)
        
        combo_box = tb.Combobox(toggle_button_ai_container, values=('Random','Min_Max'),state='readonly',textvariable=self.ai_strategy ,width=10)
        #combo_box.pack(side= LEFT, padx=10)
        combo_box.current = 0
        
        def tg(*args):        
            if(toggle_button_ai_value.get()==0):
                combo_box.pack_forget()
                player2_entry.grid(row = 2)
                self.ai=FALSE
            else:
                player2_entry.grid_forget()
                combo_box.pack(side= LEFT, padx=10)
                
                self.ai = TRUE
        
        toggle_button_ai_container
        
        return toggle_button_ai_container
    
    def create_form_entry(self, label, player_name , piece:Piece):
        form_field_container = tb.Frame(self)

        form_field_label = tb.Label(master=form_field_container, text=label)
        form_field_label.pack(side=LEFT, padx=5)

        form_input = tb.Entry(master=form_field_container, textvariable=player_name)
        form_input.pack(side=LEFT, fill=X,expand=YES)
        
        button_choose_color = tb.Button(master=form_field_container,text='Choose a Color' ,command=lambda:ccc())
        button_choose_color.pack(side=LEFT, padx=5)
        
        color_field_label = tb.Label(master=form_field_container, background=piece.color , width=3)
        color_field_label.pack(side=LEFT)
        
      
        def ccc(*args):
            my_color = ColorChooserDialog()
            my_color.show()
            if(my_color.result):
                    piece.color= my_color.result.hex
                    color_field_label.config(background=piece.color)
        
        return form_field_container
            
    def handel_click(self,main_window):
        
        player1 = Player(self.player1_name.get(), self.piece1)
        player2 = Player('AI', Piece('yellow'),TRUE)
        
        if(self.ai == FALSE):
            player2 = Player(self.player2_name.get(), self.piece2)
                
        ai = AI(self.ai_strategy.get())

        self.pack_forget()
        #self.main_window.geometry((600,800))
        player1.turn=TRUE
        Game(main_window,player1,player2,ai)
        
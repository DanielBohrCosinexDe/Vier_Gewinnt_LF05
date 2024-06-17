import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox



from model.piece import Piece
from model.player import Player

from .board import Board

from model.player import Player
class Game(tb.Frame):
    def __init__(self,main_window:tb.Window,player1:Player,player2:Player,ai):
        #init Frame
        super().__init__(main_window)
        main_window.geometry('700x654')
    
        self.player1=player1
        self.player2=player2
        self.ai = ai
        
        self.player_info = self.player_info_frame(self.player1,self.player2)
        self.boardFrame = self.board_frame()
        
        
        self.player_info.pack()
        self.boardFrame.pack()
        
        self.pack(expand=YES)
        
    #@staticmethod
    def player_info_frame(self,p1,p2):
        
        self.player1=p1
        self.player2=p2
        
        info_frame = tb.Frame(self,bootstyle="", height=50)
        info_frame.columnconfigure(2,weight=1)

        def create_player_info_box(player:Player,column,style):
            player_name_label = tb.Label(info_frame,text=player.name)
            player_Progressbar=tb.Progressbar(info_frame,bootstyle=style,mode='determinate')

            if(player.turn == True):
                player_Progressbar.start(10)
            else:
                player_Progressbar.stop()
                player_Progressbar.configure(value=100)
                
            player_name_label.grid(row=1,column=column, padx=25)
            player_Progressbar.grid(row=2,column=column, padx=25)

            return player_Progressbar

        def create_timer_box(*args):
            time_label = tb.Label(info_frame,text='00:00')
            #time_label.config(text='')
            #time_label.after(1000,'test')
            
            time_label.grid(row=2, column=2)
            
        create_player_info_box(self.player1,0,'danger')
        create_player_info_box(self.player2,9,'warning')
        
        
        create_timer_box()

        info_frame.pack_forget()
        #info_frame.pack(fill=BOTH, expand=YES,side=TOP)
        self.player_info = info_frame
        return info_frame
        
    def board_frame(self):
        board_frame = tb.Frame(self)
        Board(board_frame,self,self.player1,self.player2,self.ai)
        self.boardFrame = board_frame
        
        return board_frame

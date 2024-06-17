import pygame
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox


from model.player import Player
from model.board_grid import Board_grid
from model.ai import AI

class Board(tb.Canvas):
    def __init__(self,parent_frame,master,player1:Player,player2:Player,ai) -> None:
        
        super().__init__(parent_frame,width=700, height=600)
       
        self.master = master
        
        self.board_grid = Board_grid()
        self.parent_frame = parent_frame
        self.player1=player1
        self.player2=player2
        self.ai=ai
                
        self.current_player = self.player1 if self.player1.turn else self.player2
        
        self.grid(row=0, column=0, columnspan=7)
        self.bind("<Button>", self.handle_click)
        self.bind("<Motion>", self.handle_hover)
        self.hover_column = None
        self.draw_board()
        
    def draw_board(self):
        
        #canvas.create_oval(
            # center_x - radius, center_y - radius,
            # center_x + radius, center_y + radius, 
            # fill='blue', outline='black'
        #)
        """ canv.create_oval(150 - r, 150 - r, 150 + r, 150 + r, fill='white', outline="black")
        canv.create_oval(250 - r, 150 - r, 250 + r, 150 + r, fill='white', outline="black")
        canv.create_oval(350 - r, 150 - r, 350 + r, 150 + r, fill='white', outline="black")
        
        #canv.create_oval(150 - r, 150 - r, 150 + r, 150 + r, fill='white', outline="black")
        canv.create_oval(150 - r, 250 - r, 150 + r, 250 + r, fill='white', outline="black")
        canv.create_oval(150 - r, 350 - r, 150 + r, 350 + r, fill='white', outline="black") """
        
        radius=45
        self.delete("all")
        
        for row in range(6):
            for col in range(7):
                x = col * 100 + 50
                y = row * 100 + 50
                piece = self.board_grid.grid[row][col]
                color = "white" if piece is None else piece.color
                self.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color, outline="black")

        if self.hover_column is not None and self.hover_column < 7:
            for row in reversed(range(6)):
                if self.board_grid.grid[row][self.hover_column] is None:
                    x = self.hover_column * 100 + 50
                    y = row * 100 + 50
                    color = "pink" if self.player1.turn else "light yellow"                    
                    self.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color, outline="black")
                    break
                
    def play(*args):
        pygame.mixer.init()
        pygame.mixer.music.load("./asset/2.wav")
        pygame.mixer.music.play()
    
    def handle_click(self, event):
        #print(event)
        # // 250 // 100 = 2,5 round = 2
        print(event)
        self.play()
        if self.current_player.ai == True:
            col = event
        else:
            col = event.x // 100
        
        #self.master.boardFrame.after(1000)
        
        row = self.board_grid.drop_piece(col, self.current_player.piece)
        self.draw_board()

        if row is not None:
            self.draw_board()
            if self.board_grid.check_winner(self.current_player.piece):
                messagebox.showinfo("Game Over", f"{self.current_player.name} wins!")
                self.board_grid.initialize_board()
                self.draw_board()
                
                ####
                if self.current_player.ai == True:
                    ai = AI('random')
                    col = ai.drop_piece_random()
                    print(col)
                    self.handle_click(col)
                ####
            elif self.board_grid.is_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.board_grid.initialize_board()
                self.draw_board()
            else:
                self.switch_player()
    
    def handle_hover(self, event):
        new_hover_column = event.x // 100
        if new_hover_column != self.hover_column:
            self.hover_column = new_hover_column
            self.draw_board()


    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2
        self.player1.turn = not self.player1.turn
        self.player2.turn = not self.player2.turn

        self.master.player_info.destroy()
        
        self.master.boardFrame.pack_forget()
        
        self.master.player_info_frame(self.player1, self.player2).pack()
        
        self.master.boardFrame.pack()
        
        if self.current_player.ai == True:                        

            col = self.ai.play()
            print(col)
            self.handle_click(col)
from random import randrange

class AI():
    def __init__(self,strategy) -> None:
        self.strategy = strategy
        
        
        
    def play(self)->int:
        if self.strategy == "Min_Max":
            return 0
        else:
            return self.drop_piece_random()
            
        
    def drop_piece_random(self)->int:
        return randrange(6)
    
    def drop_piece_min_max():
        pass
    
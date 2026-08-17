# %%
import numpy as np
from TTT_base import TickTacToe



# %%
class TTT_gameplay(TickTacToe):
    
    
    def __init__(self):
        mark1 = input("Choose your mark: (Player1)")
        mark2 = input("Choose your mark: (Player2)")
        super().__init__(mark1, mark2)
        
        self.first = self.chooseFirst()
        
        
    def chooseFirst(self):
        first = np.random.choice([-1,1])
        return first
            
        
    
    def gameplay(self):
        current_player = self.first
        print(f"First player to move is : {self.number_symbol_encode[current_player]}")
        
        while not self.win:
            self.printGrid()
            print(f"Player {self.number_symbol_encode[current_player]} turn")
            row ,col = 0, 0
             
            while row < 1 or row > 3 or col < 1 or col > 3:
                move = input("Please enter again the valid grid")
                row, col = map(int, move.split()) # To convert string to int
            row -= 1
            col -= 1
            self.mark(row, col, current_player)
            self.checkWinner()
            
            current_player = -current_player
            
            
            
            

# %%
def main():
    game = TTT_gameplay()
    
    game.gameplay()
    


if __name__ == "__main__":
    main()
# %%

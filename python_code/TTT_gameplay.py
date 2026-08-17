# %%
import numpy as np
from TTT_base import TickTacToe



# %%
class TTT_gameplay(TickTacToe):
    
    
    def __init__(self):
        # mark1 = input("Choose your mark: (Player1)")
        # mark2 = input("Choose your mark: (Player2)")
        mark1 = "X"
        mark2 = "O"
        super().__init__(mark1, mark2)
        
        self.first = self.chooseFirst()
        
        
    def chooseFirst(self):
        first = np.random.choice([-1,1])
        return first
            
        
    
    def gameplay(self):
        current_player = self.first
        print(f"First player to move is : {self.number_symbol_encode[current_player]}")
        
        # self.mark(1, 2, "X")
        # self.mark(2,1,"X")
        # self.mark(0,1,"X")
        # self.printGrid()
        # self.checkWinner()
        
        
        while not self.win:
            
            print(f"Current player is : {self.number_symbol_encode[current_player]}")
            
            print("Input Row")
            row = int(input())
            print("Input Col")
            col = int(input())
            
            self.mark(row, col, self.number_symbol_encode[current_player])
            
            self.printGrid()
            print(" Pass this !!! ")
            self.checkWinner()
            
            current_player = -current_player
            
            
            
        
        
         
         
    def test(self):
        self.mark(1, 2, "X")
        self.mark(2,1,"X")
        self.mark(0,1,"X")
        self.printGrid()
        self.checkWinner()
        print(self.win)



# %%
def main():
    game = TTT_gameplay()
    game.gameplay()
    

if __name__ == "__main__":
    main()
# %%

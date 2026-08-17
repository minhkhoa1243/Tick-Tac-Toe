# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.3
# ---

# %%
from collections import defaultdict
import numpy as np
import random as rd
# %%
class TickTacToe:
    
    symbol_number_encode = defaultdict(int)
    number_symbol_encode = defaultdict(str)
    def __init__(self, mark1 = 'X', mark2 = 'O'):
        self.grid = np.array([[0] * 3 for i in range(3)])
        
        self.symbol_number_encode['_'] = 0
        self.number_symbol_encode[0] = '_'
        
        self.symbol_number_encode[mark1] = -1
        self.number_symbol_encode[-1] = mark1
        self.symbol_number_encode[mark2] = 1
        self.number_symbol_encode[1] = mark2
        

    def printGrid(self):
        for i in range(3):
            print("|", end= "")
            for j in range(3):
                print(self.number_symbol_encode[self.grid[i][j]], end="|")
            print(" ")
        print("")
            
        
    def mark(self, x, y, symbol):
        if self.grid[x][y] != 0:
            print("You can't choose this, this was occupied !!! \n Please choose again")
        else:
            self.grid[x][y] = self.symbol_number_encode[symbol] # Convert symbol to numerical values 
    
  
    
    def checkWinner(self):
        win = True
        
        # Check the horizontal
        for i in range(3):
            pre = self.grid[i][0]
            if pre == 0:
                continue
            win = True
            
            for j in range(1,3):
                if self.grid[i][j] != pre:
                    win = False
            
            if win:
                print(f"The winner is: {self.number_symbol_encode[pre]}")
                return                    
            
        # Check the vertical 
        for i in range(3):
            pre = self.grid[0][i]
            if pre == 0:
                continue
            win = True

            for j in range(1,3):
                if self.grid[j][i] != pre:
                    win = False

            if win:
                print(f"The winner is: {self.number_symbol_encode[pre]}")
                return  
            
        # Check the diagonal
        pre = self.grid[0][0]
        if pre != 0:
            win = True
            for i in range(1, 3):
                if self.grid[i][i] != pre:
                    win = False
            
            if win:
                print(f"The winner is: {self.number_symbol_encode[pre]}")
                return  
        
        # Check the diagonal 
        pre = self.grid[0][2]
        if pre != 0:
            win = True
            for i in range(1, 3):
                if self.grid[i][2 - i] != pre:
                    win = False
            
            if win:
                print(f"The winner is: {self.number_symbol_encode[pre]}")
                return  
            

    def clear(self):
        self.grid = [[0] * 3 for _ in range(3)]
    
    # TODO: implement gameplay
    def gameplay(self):
        pass


# %%
class Game(TickTacToe):    
    
    mark = ('X', 'O')
    def play(self):
        game_mode = input("Choose your game mode : \n 1. Player vs Player \n 2. Player vs Computer \n 3. Exit")
        # TODO: Implement all of this
        if game_mode == 1:
            pass
        
        elif game_mode == 2:
            pass
        
        else:
            return
        
    def PlayerVsPlayer(self):
        mark1 = input("Choose your mark X or O (P1)")  
        mark2 = 'O'  
        if mark1 == 'X':
            mark2 = 'O'
            print('So P2 will be O')
        else:
            mark2 = 'X'
            print('So P2 will be X')
            
            

        first_to_move = input("Choose the first one to take action \n 1. P1 \n 2. P2 \n 3. Random")
        if first_to_move == 1:
            first_to_move = self.symbol_number_encode[mark1]
            
        elif first_to_move == 2:
            first_to_move = self.symbol_number_encode[mark2]
            
        else:
            first_to_move = rd.choice([-1, 1])
        
    


# %%
def main():
    # mark1 = input("Choose your mark: (Player1)")
    # mark2 = input("Choose your mark: (Player2)")
    new_game = TickTacToe()
    new_game.printGrid()
    
    new_game.mark(0,0,'O')
    new_game.mark(0,1,'X')
    new_game.mark(0,2,'X')
    new_game.mark(1,1,'O')
    new_game.mark(2,2,'O')
    new_game.printGrid()
    
    new_game.checkWinner()
    print()
    
    
    
    
    
    

# %%
if __name__ == "__main__":
    main() 


# %%

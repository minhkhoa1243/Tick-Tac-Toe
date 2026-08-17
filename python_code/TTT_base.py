# %%
from collections import defaultdict
import numpy as np
import random as rd
import typing 
# %%
class TickTacToe:
    

    
    def __init__(self, mark1 = 'X', mark2 = 'O'):
        self.grid = np.array([[0] * 3 for i in range(3)])
        
        self.symbol_number_encode = defaultdict(int)
        self.number_symbol_encode = defaultdict(str)
        
        self.symbol_number_encode['_'] = 0
        self.number_symbol_encode[0] = '_'
        
        self.symbol_number_encode[mark1] = -1
        self.number_symbol_encode[-1] = mark1
        self.symbol_number_encode[mark2] = 1
        self.number_symbol_encode[1] = mark2
        self.win = False

    def printGrid(self):
        for i in range(3):
            print("|", end= "")
            for j in range(3):
                print(self.number_symbol_encode[self.grid[i][j]], end="|")
            print(" ")
        print("")
            
        
    def mark(self, x: int, y: int, symbol):
        while True:
            
            if self.grid[x][y] != 0:
                print("You can't choose this, this was occupied !!! \n Please choose again")
                print("Input row")
                x = int(input())
                print("Input col")
                y = int(input())
            else:
                self.grid[x][y] = self.symbol_number_encode[symbol] # Convert symbol to numerical values
                return
             
    
    
    def checkWinner(self):
        # Check the horizontal
        for i in range(3):
            pre = self.grid[i][0]
            if pre == 0:
                continue
            self.win = True
            
            for j in range(1,3):
                if self.grid[i][j] != pre:
                    self.win = False
            
            if self.win:
                print(f"1 The winner is: {self.number_symbol_encode[pre]}")
                return               
        
        # Check the vertical 
        for i in range(3):
            pre = self.grid[0][i]
            if pre == 0:
                continue
            self.win = True

            for j in range(1,3):
                if self.grid[j][i] != pre:
                    self.win = False

            if self.win:
                print(f"2 The winner is: {self.number_symbol_encode[pre]}")
                return  
 

        # Check the diagonal
        pre = self.grid[0][0]
        if pre != 0:
            self.win = True
            for i in range(1, 3):
                if self.grid[i][i] != pre:
                    self.win = False
            
            if self.win:
                print(f"3 The winner is: {self.number_symbol_encode[pre]}")
                return  
        
        # Check the diagonal 
        pre = self.grid[0][2]
        if pre != 0:
            self.win = True
            for i in range(1, 3):
                if self.grid[i][2 - i] != pre:
                    self.win = False
            
            if self.win:
                print(f"4 The winner is: {self.number_symbol_encode[pre]}")
                return  
        self.win = False  
          

    def clear(self):
        self.grid = [[0] * 3 for _ in range(3)]
    
    # TODO: implement gameplay
    def gameplay(self):
        pass

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

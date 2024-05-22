import random
import numpy as np
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

HORIZONTAL = "horizontal"
VERTICAL = "vertical"
DIRECTION = [HORIZONTAL, VERTICAL]

class Crossword:
    def __init__(self) -> None:
        self.grid_size = 0
        self.grid = [[]]
        self.placed_words = []
        is_crossword_empty = True

    def is_crossword_empty(self) -> bool:
        for row in self.grid:
            for element in row:
                if(element == "-"):
                    continue
                else:
                    self.is_crossword_empty = False
                    return False
        
        return True
    
    def get_word_list(self) -> list:
        word_list = ['apple','banana','orange','grape','pineapple','pomegranate']
        return word_list   

    def set_grid_size(self,size) -> int:
        self.grid_size = size

    def initialise_crossword(self) -> bool:
        self.grid = [['-'] * self.grid_size for _ in range(self.grid_size)]
        return True

    def word_present(self, x : int , y : int) -> bool:
        return True
    
    def check_place_word(self,word : str, x : int, y : int , direction : str) -> bool:
        word_len = len(word)
        #if word before
            #return False
        #if word after
            #return False
        #if word overlapping 
            #if overlapping is ok
                #return True
            #if overlapping is not ok
                #return False
        #if word out of bound
            #return False
        if(direction == HORIZONTAL):
            if(y + word_len > self.grid_size):
                logging.error(f"Error!, Can't place {word} at {x}, {y} {direction}ly")
                return False
        else:
            if(x + word_len > self.grid_size):
                logging.error(f"Error!, Can't place {word} at {x}, {y} {direction}ly")
                return False
        
        return True
    
    def find_common(self,word : str) -> None:
        pass

    def place_word(self,word,x,y,direction) -> bool:
            logging.info(f"Placing word {word} at {x} , {y} {direction}ly")
            if(direction == HORIZONTAL):
                for i, letter in enumerate(word):
                    self.grid[x][y + i] = letter
            else:
                for i, letter in enumerate(word):
                    self.grid[x + i][y]


    def generate_crossword(self) -> bool:
        word_list = self.get_word_list()
        self.set_grid_size(len(max(word_list, key=len)))
        self.initialise_crossword()
        
        for word in word_list:
            direction = random.choice(DIRECTION)
            tries = 0
            while(tries < 100): 
                x,y = random.sample(list(range(self.grid_size)),k=2)   
                if(self.check_place_word(word,x,y,direction)):            
                    self.place_word(word,x,y,direction)
                    break
                else:
                    tries +=1

if __name__ == "__main__":
    crossword = Crossword()
    print(np.matrix(crossword.grid))
    crossword.generate_crossword()
    print(np.matrix(crossword.grid))
    
import random
import numpy as np

class Crossword:
    def __init__(self) -> None:
        self.grid_size = 0
        self.grid = [[]]


    def is_crossword_empty(self) -> bool:
        for row in self.grid:
            for element in row:
                if(element == 0):
                    continue
                else:
                    return False
        
        return True
    
    #Get initial random coordinates to place first word
    def get_x_y(self,is_horizontal : bool, word_len : int, grid_size : int) -> list:
        while(1):
            x,y = random.randrange(0, grid_size ), random.randrange(0,grid_size)

            if((is_horizontal == False )and  ( grid_size - x + 1 >= word_len) ):
                return x,y
            
            elif((is_horizontal == True ) and (grid_size - y + 1 >= word_len)):
                return x,y
            
        return []

    def get_word_list(self) -> list:
        word_list = ['apple','banana','orange','grape','pineapple','pomegranate']
        return word_list

    def place_word(self,word:str,grid_size:int) -> None:
        is_horizontal = random.choice([True,False])
        # is_horizontal = False

        #First iteration when crossword is empty
        if(self.is_crossword_empty()):
            if(is_horizontal == False):
                x,y = self.get_x_y(is_horizontal,len(word),grid_size)                
                for i, letter in enumerate(word):
                    self.grid[x + i][y] = letter
            else:
                x,y = self.get_x_y(is_horizontal,len(word),grid_size)
                for i, letter in enumerate(word):
                    self.grid[x][y + i] = letter
        
        #After adding first word to crossword
        else:
            if(is_horizontal == False):
                # if(self.check_intersection(word,))
                    
                pass
            else:
                pass

    #To check if next word can be intersected with another existing word
    def check_intersection(self) -> None:
        pass

    def generate_crossword(self) -> None:
        word_list = self.get_word_list()
        grid_size = len(max(word_list, key=len))
        added_words = []
        self.grid = [[0] * grid_size for _ in range(grid_size)]
        # print(crossword)
        for word in word_list:
            self.place_word(word,grid_size)
            added_words.append(word_list.pop(0))
            print(np.matrix(self.grid))            

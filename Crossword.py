import random
import numpy as np

class Crossword:
    def __init__(self) -> None:
        self.grid_size = 0
        self.grid = [[]]
        self.placed_words = []

    def is_crossword_empty(self) -> bool:
        for row in self.grid:
            for element in row:
                if(element == 0):
                    continue
                else:
                    return False
        
        return True
    
    #Get initial random coordinates to place first word
    def get_x_y(self,is_horizontal : bool, word_len : int) -> list:
        while(1):
            x,y = random.randrange(0, self.grid_size ), random.randrange(0,self.grid_size)

            if((is_horizontal == False )and  ( self.grid_size - x - 1 >= word_len) ):
                return x,y
            
            elif((is_horizontal == True ) and (self.grid_size - y - 1 >= word_len)):
                return x,y
            
        return []

    def get_word_list(self) -> list:
        word_list = ['apple','banana','orange','grape','pineapple','pomegranate']
        return word_list

    def get_common(self,word:str, new_word:str) -> list:
        common_indices = []
        for index, char in enumerate(word):
            # Check if character is common and its index in string2
            if char in new_word:
                common_indices.append((index, new_word.index(char)))
        return common_indices
    
    def place_word(self,word:str) -> tuple:
        is_horizontal = random.choice([True,False])
        x = y = 0
        # is_horizontal = True
        #First iteration when crossword is empty
        if(self.is_crossword_empty()):
            print("Crossword is empty")
            if(is_horizontal == False):
                x,y = self.get_x_y(is_horizontal,len(word))
                # print("Coordinates are " + str(x) + "," + str(y))             
                for i, letter in enumerate(word):
                    self.grid[x + i][y] = letter
            else:
                x,y = self.get_x_y(is_horizontal,len(word))
                # print("Coordinates are " + str(x) + "," + str(y))             
                for i, letter in enumerate(word):
                    self.grid[x][y + i] = letter
        
        #After adding first word to crossword
        else:
            print("Adding next word " + word)
            if(self.check_intersection(word,is_horizontal)):
                pass
            else:
                pass
        
        return (x,y,is_horizontal,word)

    #To check if next word can be intersected with another existing word
    def check_intersection(self,new_word:str,is_horizontal_new:bool) -> None:
        # words_filtered = filter(lambda word : word[2] == True) #Check direction, 2nd pos in tuple
        for word in self.placed_words:
            if(word[2] == False and is_horizontal_new == True): #if cross with vertical word
                cmn_idx = self.get_common(word[3],new_word)
                # new_word_start = 
                print(cmn_idx)
                pass

        print()
        pass

    def generate_crossword(self) -> None:
        word_list = self.get_word_list()
        self.grid_size = len(max(word_list, key=len))
        # added_words = []
        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        # print(crossword)
        for word in word_list:
            word_tup = self.place_word(word) #x,y,direction,word
            self.placed_words.append(word_tup)
            word_list.pop(0)
            # print(word_tup)
            
        print(np.matrix(self.grid))            

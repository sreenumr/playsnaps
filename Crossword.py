import random
import numpy as np
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

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
        for index1, char1 in enumerate(word):
            for index2, char2 in enumerate(new_word):
            # Check if character is common and its index in string2
                if char1 == char2:
                    common_indices.append((index1, index2))
        return common_indices
    
    def place_word(self,word:str) -> tuple:
        is_horizontal = random.choice([True,False])
        x = y = 0
        # is_horizontal = True
        #First iteration when crossword is empty
        if(self.is_crossword_empty()):
            logging.info("Crossword is empty, adding word " + word)
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
            logging.info("Adding next word "+ word)
            if(self.check_intersection(word,is_horizontal)):
                pass
            else:
                pass
        
        return (x,y,is_horizontal,word)

    #To check if next word can be intersected with another existing word
    def check_intersection(self,new_word:str,is_horizontal_new:bool) -> None:
        # words_filtered = filter(lambda word : word[2] == True) #Check direction, 2nd pos in tuple
        for word in self.placed_words:
            if(word[2] == False and is_horizontal_new == True): #new word horizontal X vertical
                cmn_idx = self.get_common(word[3],new_word)
                # new_word_start = 
                logging.info(f"Common Index = {str(cmn_idx)}")
                pass
            elif(word[2] == True and is_horizontal_new == False): #new word vertical X horizontal
                cmn_idx = self.get_common(word[3],new_word)

                logging.info(f"Common Index = {str(cmn_idx)}")

        pass

    def generate_crossword(self) -> None:
        word_list = self.get_word_list()
        self.grid_size = len(max(word_list, key=len))
        # added_words = []
        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        # logging.info(crossword)
        for word in word_list:
            word_tup = self.place_word(word) #x,y,direction,word
            self.placed_words.append(word_tup)
            # word_list.pop(0)
            # logging.info(word_tup)
            
        logging.info(np.matrix(self.grid))            

import random

class Crossword:
    def __init__(self,grid_size : int) -> None:
        self.grid_size = grid_size
        self.matrix = [[]]

    def is_empty(self) -> bool:
        for row in self.matrix:
            for element in row:
                if(element == 0):
                    continue
                else:
                    return False
        
        return True
    
    def get_word_list() -> None:
        word_list = ['apple','banana','orange','grape','pineapple','pomegranate']
        return word_list

    def add_word(word:str) -> None:
        pass

    def check_intersection(self) -> None:
        pass

    def generate_crossword(self) -> None:
        word_list = self.get_word_list()
        grid_size = len(max(word_list, key=len))
        horizontal = random.choice([True,False])
        added_words = []
        crossword = [[0] * grid_size for _ in range(grid_size)]
        print(crossword)
        # for word in word_list:
        #     if(is_empty(crossword)):
        #         start_pos = random.randrange(0,grid_size)
        #     if(horizontal == True):
        #         start_pos = random.randrange(0,grid_size)
                
        #     else:

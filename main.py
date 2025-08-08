import random
import requests
import os


class Worlde :
    def __init__(self, word_length = 5 , max_attempts = 6):
        self.word_length = word_length 
        self.max_attempts = max_attempts
        self.selected_word = self.select_word(word_length)



    def select_word(self,word_length) :                               #passed as a parameter to reduce dependency 
        file_name = f'{word_length}-letter-words.txt'                 #3-letter-words.txt , 4-letter-words.txt
        folder_path = os.path.dirname(os.path.abspath(__file__))      
        file_path = os.path.join(folder_path,file_name)               #full_path -> no need to run from the folder place
        
        #reading file
        with open(file_path) as f :                                   #storing all words in memory to fetch from it instead of file -> faster
            self.words = f.read().splitlines()                        #splits by \n default , self. to be used by other methods
        self.n_of_words = len(self.words)                             #much more words than API -> even bigger datasets can be used

        #picking a random word
        selected_word_index = random.randint(0,self.n_of_words)
        return self.words[selected_word_index]



    

wordle = Worlde()
print(wordle.selected_word)

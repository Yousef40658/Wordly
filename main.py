import random
import requests


class Worlde :
    def __init__(self, word_length = 5 , max_attempts = 6):
        self.word_length = word_length 
        self.max_attempts = max_attempts
        selected_word = self.select_word(word_length)



    def select_word(self,word_length) :                               #passed as a parameter to reduce dependency 
        #Dataset
        pattern = "?" * word_length                                   #n? returns words with n letters
        url = f"https://api.datamuse.com/words?sp={pattern}&max=1000" #maximum 1000 words , #builds url
        response = requests.get(url)                                  #request to the API and getting response 
        words = response.json()                                        #parses the response into a dictonery

        n_of_words = len(words) #for_safety
        selected_word_index = random.randint(0,n_of_words)
        selected_word = words[selected_word_index]["word"]
        print(selected_word)
        return selected_word

    

wordle = Worlde()

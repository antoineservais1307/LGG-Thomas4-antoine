import random
from typing import List
class Hangman():

    def __init__(self) -> None:
        self.possible_word: List[str]  = ['becode','learning','mathematicsc','sessions','denis','cindy','antoine','nicolas']
        self.word_to_find: List[str] = list(random.choice(self.possible_word))
        self.lives: int = 5
        self.correctlly_guessed_letters: List[str] = []
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

    def play(self):

        guessed_letter = input("Enter a letter to guess the word : ")
        while not guessed_letter.isalpha() or len(guessed_letter) > 1 or guessed_letter in self.correctlly_guessed_letters or  guessed_letter in self.wrongly_guessed_letters and self.lives > 0:
            if not guessed_letter.isalpha():
                guessed_letter = input("Enter a letter please :")
            elif len(guessed_letter) > 1:
                guessed_letter = input("Enter only one letter at a time please :")
            elif guessed_letter in self.correctlly_guessed_letters:
                guessed_letter = input(guessed_letter, "was already submmitted and in the word, enter another letter please :")
            elif guessed_letter in self.correctlly_guessed_letters:
                guessed_letter = input(guessed_letter, "was already submitted and was not in the word")
                return guessed_letter
            if guessed_letter in self.word_to_find:
                for j in self.word_to_find:
                    if j == guessed_letter:
                        self.correctlly_guessed_letters.append(guessed_letter)
                    else: 
                        self.correctlly_guessed_letters.append("_")
                print(self.correctlly_guessed_letters)
                return self.correctlly_guessed_letters
            else:
                self.lives = self.lives - 1
                self.wrongly_guessed_letters.append(guessed_letter)
                print(self.wrongly_guessed_letters)
                return self.wrongly_guessed_letters, self.lives
        if self.lives == 0:
            print("No more life to play, GAME OVER")
        
                    
                
                


hangman = Hangman()
hangman.play()
from typing import List

def get_word() -> str:  
    """
    function to take a word to play in param

    :return secret_world : return the word to guess
    """

    secret_word = input("Enter a word you want to be guessed : ")
    return secret_word

def get_lives() -> int: 
    """
    function to take a number of lives to play in param

    :return lives : return the number of lives to play
    """

    lives = int(input("Enter a number of lives for the player : "))
    return lives

def get_guess(suggested_letters: List[str]) -> List[str]:
    suggested_letter = input("Enter a letter you want to guess : ")
    """
    function that ask the player to enter a letter to guess the word, and verifies if the letter is in the correct parameter in params
    
    :param suggested_letter : ask the player for a letter
    :param suggested_letters : a list of all the letter the player asked
    :return suggested_letters : return the list of all the latter played
    """

    while not suggested_letter.isalpha() or len(suggested_letter) > 1 or suggested_letter in suggested_letters:
        if not suggested_letter.isalpha():
            suggested_letter = input("Please enter only letter : ")
        elif len(suggested_letter) > 1: 
            suggested_letter = input("Enter only one letter at a time : ")
        else:
            suggested_letter = input("Letter already submmitted, enter another one : ")
    
    suggested_letters.append(suggested_letter)
    return suggested_letters
    
       
def assess_guess(secret_word: str, guessed_letter: str, lives_lefts: int) -> int:
    """
    function that check the amount of lives lefts to play in param
    
    :param guessed_letter : last letter played to check if it's correct or no
    :return lives_left : new amount of lives to play
    """

    if not  guessed_letter in list(secret_word):
        lives_lefts -= 1
    return lives_lefts

def display_word(secret_word: str, suggested_letters: List[str]) -> bool:
    """
    function to display the letters of the word that are already guessed and replace the other one with a blank space in param
    

    """
    word = []
    for i, j in enumerate(list(secret_word)):
        if j in suggested_letters:
            word.append(j)
        else: 
            word.append("_")

    print("".join(word))

    if "_" in word:
        return True
    else:
        return False
        
    

if __name__ == "__main__":
    suggested_letters: List[str] = []
    secret_word: str = get_word()
    lives_lefts: int = get_lives()   

    while display_word(secret_word, suggested_letters) and lives_lefts != 0:
        suggested_letters = get_guess(suggested_letters)
        lives_lefts = assess_guess(secret_word,suggested_letters[-1],lives_lefts)
    
    if lives_lefts > 0:
        print("You win !")
    else:
        print("You loose, the word was : ", secret_word)


import random
#import words.txt and make into a list
# ask user for mode "Easy", "Normal", "Hard"

class Word:
    def __init__(self):
        word_list = open(words.txt)
        word_list = word_list.read()
        self.word = random.choice(word_list.read)
        # self.word_length = word_length 
        # use word_length to build a function for difficulty: "easy", "normal" or "hard" levels
        # return word.upper()
 
    def show_mystery_word(self):
        return '_ ' * len(self)


#https://stackoverflow.com/questions/60617366/how-to-reveal-a-specific-letter-in-a-string-for-python

class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def attempt_guess(self):
        total_guesses= 8
        guesses = 0
        word = Word()
        gameboard = show_mystery_word(word)
        print(gameboard)
        gameboard = list(gameboard)
        while guesses < total_guesses:
            guess = input("Please guess a letter: ")
            if guess.lower() not in word:
                guesses += 1
                print("Incorrect, guesses remaining:", total_guesses - guesses, "Try again.")
            else: 
                print("Correct!")
           
            for letter in word:
                if guess.lower() == letter:
                    gameboard[word.index(letter) * 2] = guess.lower()
                  
            print("".join(gameboard))
            print(guesses)
            if not "_" in gameboard:
                print("Congratulations, You win! Would you like to play again?")

def show_mystery_word(Word.word):
    return '_ ' * len(word)

difficulty = input("Do you want to play difficulty level Easy, Normal, or Hard? ")
new_game = Game(difficulty)
new_game.attempt_guess()


    
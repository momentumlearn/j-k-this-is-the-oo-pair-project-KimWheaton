
#import random
#import words.txt



#ask user for mode "Easy", "Normal", or "Hard"



attemps = 8

word = "SPAM"
print("Welcome to Wheel of Fortune!")

#display the number of letters in word
def show_mystery_word(word):
    return '_ ' * len(word)
# print(show_mystery_word(word))
# print("")

#https://stackoverflow.com/questions/60617366/how-to-reveal-a-specific-letter-in-a-string-for-python
def attempt_guess():
    total_guesses= 8
    guesses = 0
    gameboard= show_mystery_word(word)
    print(gameboard)
    gameboard = list(gameboard)
    while guesses < total_guesses:
        guess = input("Please guess a letter: ")
        if guess.upper() not in word:
            guesses += 1
            print("Incorrect, guesses remaining:", total_guesses - guesses, "Try again.")
        else: 
            print("Correct!")
           
            for letter in word:
                if guess.upper() == letter:
                    gameboard[word.index(letter) * 2] = guess.upper()
                
               
            print("".join(gameboard))
            print(guesses)
            if not "_" in gameboard:
                print("Congratulations, You win! Would you like to play again?")
attempt_guess()
print()
    





# ask user for mode ("Easy", "Normal", "Hard")

########new code ideas to plug into shared program ######################
# import random
# import words.txt

# def get_word():
    # word = random.word_list


word = "GOOGLE"
def show_mystery_word(word):
    return " - " * len(word)
print(show_mystery_word(word))


#import random
#import words.txt



#ask user for mode "Easy", "Normal", or "Hard"


# class Word:
#   def __init__(self):

#   def get_word():
        # word = random.choice(word_list) - is this what it's named?
        # return word.upper()

attemps = 8

word = "GOOGLE"
print("Welcome to Wheel of Fortune!")

#display the number of letters in word
def show_mystery_word(word):
    return ' _ ' * len(word)
print(show_mystery_word(word))
print("")

#https://stackoverflow.com/questions/60617366/how-to-reveal-a-specific-letter-in-a-string-for-python
def attempt_guess():
    total_guesses= 8
    guesses = 0
    gameboard = show_mystery_word(word)
    print(gameboard)
    while guesses < total_guesses:
        guess = input("Please guess a letter: ")
        if guess.upper() not in word:
            guess += 1
            print("Incorrect, guesses remaining:", total_guesses - guesses, "Try again.")
        else: 
            print("Correct!")
            new_gameboard = ''
            for w,l in zip(word, gameboard):
                if guess.upper() == w:
                    new_gameboard += guess.upper()
                else:
                    new_gameboard += l
            gameboard= new_gameboard
            print(gameboard)
            if not " _ " in gameboard:
                print("Congratulations, You win! Would you like to play again?")
attempt_guess()
print()
    
    #################################################

# guess = input("Please guess a letter:  ").upper()



# if guess not in word:
#     print(guess "is not in the word.")
#     tries -= 1
#     guessed_letters.append(guess)
# else:
#     print("Good job!")
#     tries -= 1
#     guessed_letters.append(guess)    


# while tries > 0:
#     for guessed_letters in guess:
#         print(guessed_letters)
#     else:
#         print('_') 
        

# if failed == 0:
#     print("Congradulations, you win! would you like to play agian?" ) 

         





# def show_word(word):
#     for i in range(0, len(word)):
#         if ord(word[i]) != 32:
#             new_word = word.replace(word[i]   qAZ , '_')
#     print(new_word)


# For character in word:
#     if character in guesses:
#         print("_"character "_")
#     else:
#         print("_")

#function to play game
#def play_game():

#ask for user input /print statement to guess letter

#user inputs guess

#return whether the letter is in the word or not

#if true: return the word with the remaining letters to be guessed

#if false return "incorrect, guess again.
# show_word(word)



# # display number of letters in word


# def show_word(word):
#     for i in range(0, len(word)):
#         if ord(word[i]) != 2:
#             new_word = word.replace(word[i], '_')
#     print(new_word)

# for character in word:
#     if character in guess:
#         print("_" character "_")
#     else:
#         print("_")

#########################################################################




#function to play game
# # def play_game(): -- 

# ask for user input /print statement to guess letter

# user inputs guess

#return whether the letter is in the word or not
# if true: return the word with the remaining letters to be guessed

# if false: return "incorrect, guess again"

# show_word(word)


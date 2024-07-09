import random
from word_list import word_list # this import the word_list function from the word_list file

def get_word():
    word = random.choice(word_list) # gets the random word from the word_list 
    return word.upper() # puts the word in uppercase (e.g: ABCD)

def play(word):
    word_completion = "_" * len(word) # displays the length of the word
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6 # Number of lives a user is given at start of the game
    print("Let's play Hangman! :-)")
    print(hangman_image(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        user_guess = input("Please guess a letter or word: ").upper()
        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in guessed_letters:
                print("You already guessed the letter - ", user_guess)
            elif user_guess not in word:
                print(user_guess, "is not in the word!")
                tries -= 1 # take a live away when user guessed incorrectly letter
                guessed_letters.append(user_guess)
            else:
                print("Good guess, ",user_guess, "is in the word!")
                guessed_letters.append(user_guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == user_guess]
                for index in indices:
                    word_as_list[index] = user_guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(user_guess) == len(word) and user_guess.isalpha():
            if user_guess in guessed_words:
                print("You already guessed the word", user_guess)
            elif user_guess != word:
                print(user_guess, "is not the word!")
                tries -= 1 # takes a live away if user guessed the word incorrectly
                guessed_words.append(user_guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess!")
        print(hangman_image(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulation you guessed the correct word!")
    else:
        print("Sorry, you ran out of tries. The correct word was " + word + ", maybe next time!")

def hangman_image(tries): # Showcase 6 pictures illustrating the progression of a hangman as the user makes incorrect guesses.
    stages = [  """
                    _________
                    |       |
                    |       O
                    |      \\ /
                    |       |
                    |      | |
                    -
                """,
                """
                    _________
                    |       |
                    |       O
                    |      \\ /
                    |       |
                    |      |
                    -
                """,
                """
                    _________
                    |       |
                    |       O
                    |      \\ /
                    |       |
                    |      
                    -
                """,
                """                    
                    _________
                    |       |
                    |       O
                    |      \\ /
                    |       
                    |      
                    -
                """,
                """                    
                    _________
                    |       |
                    |       O
                    |      \\ 
                    |       
                    |      
                    -
                """,
                """
                    _________
                    |       |
                    |       O
                    |      
                    |       
                    |      
                    -
                """,
                """                    
                    _________
                    |       |
                    |       
                    |      
                    |       
                    |      
                    -
                """
    ]
    return stages[tries]

def main(): # gets the game going
    word = get_word()
    play(word)
    while input ("Play again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
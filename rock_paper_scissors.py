import random
import time # time module is imported for the use of countdown to the next selection of each rounds

def get_user_choice(): # get_user_choice function is created to employ the user inputs of the game
    user_input = input("What's your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors\n").lower()
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'} # dictoraries with key : value
    if user_input in choices:
        user_choice = choices[user_input]
        print(f"You chose: {user_choice}") # displays the User's choice
        return user_choice
    else:
        print("\nInvalid choice! Please enter 'r', 'p', or 's'.") # this statement is printed if user selected an invalid choice
        return get_user_choice()

def get_computer_choice(): # get_computer_choice function is created for computer to give random choice
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    print(f"The Computer's choice is: {computer_choice}")
    return computer_choice

# get_winner function is created to decide the game
def get_winner(user_choice, computer_choice):
    '''
    The way that the Rock, Paper and Scissors game will be decided is by creating a if statement loop,
    so if a user choose one option (e.g Rock) and the computer choose one random option (e.g Scissors),
    who wills the game/ round (e.g User Wins)

    Returns:
    --------
    User Choose Rock and Computer choose Rock then It's a Tie!
    User Choose Rock and Computer choose Scissors then User Wins!
    User Choose Rock and Computer choose Paper then Computer Wins!
    User Choose Paper and Computer choose Paper then It's a Tie!
    User Choose Paper and Computer choose Rock then User Wins!
    User Choose Paper and Computer choose Scissors then Computer Wins!
    User Choose Scissors and Computer choose Scissors then It's a Tie!
    User Choose Scissors and Computer choose Rock then User Wins!
    User Choose Scissors and Computer choose Paper then Computer Wins!

    '''

    if user_choice == computer_choice:
        return "Tie"
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            return "User" 
        else:
            return "Computer"
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            return "User"
        else:
            return "Computer"
    elif user_choice == "Scissors":
        if computer_choice == "Paper":
            return "User" 
        else:
            return "Computer"

def play():
    user_wins = 0
    computer_wins = 0
    winning_score = 3 # First player to get 3 wins, wins the match

    while user_wins < winning_score and computer_wins < winning_score:
        # countdown timer is set to 3 seconds at the start of each rounds 
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        
        # Below text will be displayed as a way to start each round
        print("\nRock ...")
        print("Paper ...")
        print("Scissors...")
        print("Go!\n")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = get_winner(user_choice, computer_choice)

        # point given to each players
        if result == "User":
            user_wins += 1 
            print("\nYou Won this round!")
        elif result == "Computer":
            computer_wins += 1
            print("\nYou Lost this round!")
        else:
            print("\nIt's a Tie!") # no point given if it's a tie

        # displays the points given to each players
        print(f"User Score: {user_wins} Computer Score: {computer_wins}")
        print("\n")

    # player with most wins (e.g 3 wins) will win the match
    if user_wins > computer_wins:
        print("You Won the Match!")
    elif user_wins < computer_wins:
        print("Computer Won the Match!")
    else: 
        print("It's a Tie!")

    # Below while loop is used if User wants to play again or end the game
    while True:
        play_again = input("\nPlay again: Yes(y) or No(n): ")
        if play_again.lower() == "y": # continue to play the game and reset the score to 0 - 0
            play()
        else:
            play_again.lower() == "n" # end the game
            print("\nGame Over!")
            break

play()
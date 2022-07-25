import random

scores = []
player_name = input("What is your name, Player 1?  ")
print("Welcome to the matrix, {}. Step up to the challenge!".format(player_name))

def start_game():

    attempts = 0
    random_number = random.randint(1, 10)

    if scores:
        print("The current highest score is {}. Try to beat it!".format(min(scores)))

    while True:
        try:
            guess = int(input("Please guess a number between 1 and 10!  "))
            break
        except ValueError:
            print("Opps! That was not valid! Please try again!")

    while True:
        try:
            if guess == 0:
                guess = int(input("Oops! Zero isn't a valid choice. We won't count this towards your attempts. Please choose a number between 1 and 10!  "))
            elif guess > 10:
                guess = int(input("Oops! That number is higher than 10. We won't count this towards your attempts. Please choose a number between 1 and 10!  "))
            elif guess == random_number:
                print("You got it {}! Great job!".format(player_name))
                attempts += 1
                print("It took you {} attempts to guess the correct answer!".format(attempts))
                scores.append(attempts)
                if attempts == min(scores):
                    print("Congrats! You have the current highest score of {} attempts!".format(attempts))
                play_again = input("Would you like to play again? Y/N  ")
                if play_again.lower() == "y":
                    start_game()
                elif play_again.lower() == "n":
                    print("Have a wonderful day and thank you for playing, {}!".format(player_name))
                    quit()
            elif guess < random_number:
                guess = int(input("It's lower than the solution! Try again!  "))
                attempts += 1
                continue
            elif guess > random_number:
                guess = int(input("It's higher than the solution! Try again!  "))
                attempts += 1
                continue
        except ValueError:
            print("Oops! That was not valid! Please try again!")        

start_game()

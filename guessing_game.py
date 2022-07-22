import random

player_name = input("What is your name, Player 1?  ")
print("Welcome to the matrix, {}. Step up to the challenge!".format(player_name))

def start_game():

    attempts = 0
    random_number = random.randint(1, 10)

    try:
        guess = int(input("Please guess a number between 1 and 10!  "))
    except ValueError:
        guess = int(input("Please use a VALID number between 1 and 10!  "))
    if guess == 0:
        guess = int(input("Oops! Zero isn't a valid choice. We won't count this towards your attempts. Please choose a number between 1 and 10!  "))
    if guess > 10:
        guess = int(input("Oops! That number is higher than 10. We won't count this towards your attempts. Please choose a number between 1 and 10!  "))

    while True:

        if guess == random_number:
            print("You got it {}! Great job!".format(player_name))
            attempts += 1
            print("It took you {} attempts to guess the correct answer!".format(attempts))
            print("Have a wonderful day and thank you for playing, {}!".format(player_name))
            break
        elif guess < random_number:
            guess = int(input("It's lower than the solution! Try again!  "))
            attempts += 1
            continue
        elif guess > random_number:
            guess = int(input("It's higher than the solution! Try again!  "))
            attempts += 1
            continue

start_game()

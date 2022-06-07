from art import logo

from random import randint  # or import random

HARD_LEVEL_DIFFICULTY = 5
EASY_LEVEL_DIFFICULTY = 10


def game():
    def guess_the_number(computer_guess, player_guess):
        if computer_guess < player_guess:
            print("Too High!")
        elif computer_guess > player_guess:
            print("Too Low!")
        else:
            print(f"Correct, the number was {computer_guess}.")

    def number_of_turns():
        if level == "easy":
            return EASY_LEVEL_DIFFICULTY
        else:
            return HARD_LEVEL_DIFFICULTY

    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    computer_guess = randint(1, 100)

    # print(f"Psst, the number is {computer_guess}")

    player_guess = 0
    turns = number_of_turns()

    end_game = True
    while end_game and computer_guess != player_guess:

        print(f"You have {turns} turns left.")
        player_guess = int(input("Guess the Number: "))
        guess_the_number(computer_guess, player_guess)
        # print("Guess Again")
        turns -= 1
        if turns == 0:
            print(f"You ran out of guesses. Number was {computer_guess}.")
            end_game = False
        elif computer_guess != player_guess:
            print("Guess Again!")


game()

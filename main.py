
from random import *
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess,answer,turns):
    if guess > answer:
        print("Your guess is too high")
        return turns - 1
    elif guess < answer:
        print("your guess is too low")
        return turns - 1
    else:
        print("your guess is right.")


def check_level():
    level=input("Type 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS


def playgame():

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)
    print(f"psst the answer is {answer}")

    turns = check_level()
    should_continue = False
    while not should_continue:
        guess = int(input("Guess number is:"))

        Guess = check_answer(guess,answer,turns)
        turns -=1
        if guess == answer:
            should_continue = True
        if guess != answer:
            print(f"you have {turns} attempts to try again.")
            print("Guess Again")

        if turns == 0:
            print("you run out of turns,Start again")
            should_continue = True

playgame()
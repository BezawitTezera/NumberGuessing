from ASCII_art import art
from random import randint

print(art)

DifficultyLevel = input("Choose a difficulty level. For hard mode type 'Hard' for easy mode type 'Easy': ").lower()


def check(lives):
    ComputerNumber = randint(1, 100)
    if DifficultyLevel == 'hard':
        lives = 5
    elif DifficultyLevel == 'easy':
        lives = 10
    else:
        print("Enter a valid key.")

    while lives > 0:
        GuessNumber = int(input("Guess a number between 1-100: "))
        if ComputerNumber == GuessNumber:
            print(f"You won, {GuessNumber} is the generated number")
            break
        elif ComputerNumber > GuessNumber:
            lives -= 1
            print("Too Low")
            print(f"You have {lives} lives left.")
        else:
            lives -= 1
            print("Too High")
            print(f"You have {lives} lives left.")

    if lives == 0:
        print("Game Over!")
    else:
        pass


check(lives=0)

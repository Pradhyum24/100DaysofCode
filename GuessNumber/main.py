import  random
from art import logo
def game():
    print(logo)
    NUM=random.randint(1,100)
    print(NUM)
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100")
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard'").lower()

    if difficulty=="easy":
        attempts=10
    else:
        attempts=5

    while attempts!=0:
        guess = int(input(f"You have {attempts} attempts remaining to guess the number:"))
        if guess==NUM:
             print(f"You got it! The answer was {guess}.")
             attempts=0
        elif guess > NUM:
            print("Too high.")
            attempts-=1
        else:
             print("Too low.")
             attempts -= 1
    if(attempts==0):
        print("You ran out of choices")
game()








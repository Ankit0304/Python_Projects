# Guess the number mini game 

import random
def Guess_Number():
    Number = random.randint(1,50)
    
    print("I'm thinking of a number between 1 and 50")
    print("Can you guess what it is?")
    # chances to guess the number
    chances=1
    
    while chances<=5:
        Guess = int(input(f"Attempt {chances}: Enter your guess: "))
        # check if the guess is equal to the number
        if Guess == Number:
            print(f"Congratulations! You guessed the number.{Number}")
            break
        # check if the guess is higher than the number
        elif Guess>Number:
            print("Your guess is too high")
            print("Try again")
        # check if the guess is lower than the number
        else:
            print("Your guess is too low")
            print("Try again")
           
        chances+=1
        # check chances are run out or not
        if chances>5:
            print("Sorry! You're run out of chances")
            print(f"Better luck next time \nThe number was {Number}")


while True:
    Guess_Number()
    # ask user to play again
    play_again=input("Do you want to play again? (y/n): ")
    if play_again.lower()!='y':
        print("Thank you for playing!")
        break    
    
    
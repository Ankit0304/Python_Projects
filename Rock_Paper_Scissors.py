import random

while True:
    print("Welcome to Rock, Paper, Scissors Game")
    print("Choose one of the following:")
    print('''1. Rock
2. Paper
3. Scissors''')
    user=int(input("Enter your choice: "))
    while user>3 or user<1:
        print("Invalid input! Please enter a valid input")
        user=int(input("Enter valid input: "))
    
    if user==1:
            user_choice='Rock'
    elif user==2:
            user_choice='Paper'
    else:
            user_choice='Scissors'
            
    print(f"Your choice is: {user_choice}")
    print("Now it's computer's turn")
    computer=random.randint(1,3)
    if computer==1:
        computer_choice='Rock'
    elif computer==2:
        computer_choice='Paper'
    else:
        computer_choice='Scissors'
        
    print(f"Computer's choice is: {computer_choice}")
    
    if user==computer:
        print("It's a tie!")
    elif user==1 and computer==2 or user==2 and computer==3 or user==3 and computer==1:
        print("Computer wins!")
    else:
        print("You win!")
    
    play_again=input("Do you want to play again? (y/n): ")
    if play_again.lower()!='y':
        print("Thank you for playing!")
        break
    
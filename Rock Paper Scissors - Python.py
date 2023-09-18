import random

options = ("rock", "paper", "scissors")
running = True

#while running is true
#reason why you don't do while running == True is because if you have a lot of code within the while loop, it can be hard to find where the break statement is
#using a boolean is easier because you can highlight "running" and it will highlight instance where we use this "running" variable
##if you want to rename of the variable, right click on the variable and click refactor
while running:

    player = None
    computer = random.choice(options)

    #if player doesn't pick an option within "options"
    #the next block of code won't continue until it receives a valid option
    while player not in options: 
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == " scissors" and computer == "paper":
        print("You win!")
    else: #if it is none of the above, then print "you lose"
        print("You lose!")

    if not input("Do you want to play again? (y/n)").lower() == "y":
        running == False

print("Thank you for playing!")        


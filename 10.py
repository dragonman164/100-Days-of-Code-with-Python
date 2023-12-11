# Rock paper Scissors 

# Computer (Output krega)
# Player (Input lelo player se)

computerScore, playerScore = 0, 0
computersMove = 0 # (0, 1, 2)
# 0-> R, 1-> P, 2-> S
# 5 Round 
for i in range(5):
    userInput = input("Enter one of (R/P/S)?")
    if userInput == "R":
        if computersMove == 0:
            continue
        elif computersMove == 1:
            computerScore += 1
        else: 
            playerScore += 1

    elif userInput == "P":
        if computersMove == 0: 
            playerScore += 1
        elif computersMove == 1:
            continue 
        else: 
            computersMove += 1
    elif userInput == "S":
        if computersMove == 0:
            computerScore += 1  
        elif computersMove == 1: 
            playerScore += 1
        else: 
            continue

    else:
        print("Invalid Input")
        exit(0)

    computerScore += 1
    computerScore %= 3

if playerScore > computerScore:
    print("Congo , you win")
elif computerScore > playerScore:
    print("You Lose")
else: 
    print("Tie !!! ")
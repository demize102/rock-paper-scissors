playercount = input("1 or 2 players?")

if playercount == "1":
    import random
    computer = random.randint(1, 3)
    choice = input("rock, paper, or scissors?")
    if choice == "rock":
        if computer == "rock":
            print("tie!")
        elif computer == "paper":
            print("you lose!")
        else:
            print("you win!")
    elif choice == "paper":
        if computer == "rock":
            print("you win!")
        elif computer == "paper":
            print ("tie!")
        else:
            print("you lose!")
    elif choice == "scissors":
        if computer == "paper":
            print("you win!")
        elif computer == "rock":
            print("you lose!")
        else:
            print("Tie!")
    elif choice == "auto win":
        print("you win")
    elif choice == "auto lose":
        print("you lose!")
    elif choice == "gun":
        print("you win!")
    elif choice == "zeus":
        print("lightning!")
    elif choice == "c4":
        print("kaboom!")
    else:
        print("check spelling dumbass")
if playercount == "2":
    p1 = input("rock, paper, or scissors?")
    for i in range (100):
        print(" ")
    p2 = input("rock, paper, or scissors?")
    for i in range (100):
        print (" ")
    if p1 == "rock":
        if p2 == "paper":
            print("player 1 chose rock. player 2 chose paper. player 2 wins!")
        elif p2 == "rock":
            print("both players chose rock. it's a tie!")
        elif p2 == "scissors":
            print("player 1 chose rock. player 2 chose scissors. player 1 wins!")
        else:
            print("check spelling idiot")
    elif p1 == "paper":
        if p2 == "rock":
            print("player 1 chose paper. player 2 chose rock. player 1 wins")
        elif p2 == "paper":
            print("both players chose paper. it's a tie!")
        elif p2 == "scissors":
            print("player 1 chose paper. player 2 chose scissors. player 2 wins!")
        else:
            print("check spelling idiot")
    elif p1 == "scissors":
        if p2 == "rock":
            print("player 1 chose scissors. player 2 chose rock. player 2 wins!")
        elif p2 == "paper":
            print("player 1 chose scissors. player 2 chose paper. player 1 wins!")
        elif p2 == "scissors":
            print("both players chose scissors. it's a tie!")
        else:
            print("check spelling idiot")
    else:
        print("check spelling dumbass")

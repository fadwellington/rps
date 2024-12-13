import random

wins = 0
losses = 0
ties = 0

def score(result):
    global wins, losses, ties #access the global variable to update the scores
    if result == "win":
        wins += 1
    elif result == "lose":
        losses += 1
    elif result == "tie":
        ties += 1

def play():
    options = ["rock", "paper", "scissors"]
    opponent = random.randrange(len(options))
    opp = options[opponent]
    print("Welcome to Rock, Paper, Scissors!")
    player = input("Enter your choice:\n").lower()
    if player not in options:
        print("Please rock, paper, or scissors.")
    else:
        print("You chose " + player)
        print("Your opponent chose " + opp)
    def rock():
        if player == "rock" and opp == "scissors":
            print("Rock beats scissors, you win!")
            score("win")
        elif player == "rock" and opp == "paper":
            print("Paper covers rock, you lose!")
            score("lose")
        elif player == "rock" and opp == "rock":
            print("Both chose rock, it's a tie!")
            score("tie")
    def paper():
        if player == "paper" and opp == "rock":
            print("Paper covers rock, you win!")
            score("win")
        elif player == "paper" and opp == "scissors":
            print("Scissors cuts paper, you lose!")
            score("lose")
        elif player == "paper" and opp == "paper":
            print("Both chose paper, it's a tie!")
            score("tie")
    def scissors():
        if player == "scissors" and opp == "paper":
            print("Scissors cuts paper, you win!")
            score("win")
        elif player == "scissors" and opp == "rock":
            print("Rock beats scissors, you lose!")
            score("lose")
        elif player == "scissors" and opp == "scissors":
            print("Both chose scissors, it's a tie!")
            score("tie")
    rock()
    paper()
    scissors()
    print(f"\nCurrent score: Wins: {wins}, Losses: {losses}, Ties: {ties}")
    again = input("\nWould you like to play again? Yes/No\n")
    if again.lower() == "yes":
        play()
    elif again.lower() == "no":
        print("Thanks for playing!")
    else:
        print("I didnt get that, please try again later.")
play()

""" Ques 8: Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock"""

Player1 = input("Enter name of player 1: ")
Player1 = Player1.capitalize()
Player2 = input("Enter name of player 2: ")
Player2 = Player2.capitalize()

player1_input = input(f"Enter player1's input (Rock/Paper/Scissor): ").lower()
player2_input = input("Enter player2's input (Rock/Paper/Scissor): ").lower()

# game conditions

if player1_input == "rock" and player2_input == "scissors":
    print(f"{Player1} wins!")
    
elif player1_input == "scissors" and player2_input == "paper":
    print(f"{Player1} wins!")
    
elif player1_input == "paper" and player2_input == "rock":
    print(f"{Player1} wins!")
    
elif player1_input == player2_input:
    print(f"Both {Player1} and {Player2} wins!")
    
else:
    print(f"{Player2} wins!")

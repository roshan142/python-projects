#Rock paper scissors game 26/3/24
import random
game = ["rock","paper","scissors"]
def get_choices():
    player_choice = input("Enter a Choice(Rock/Paper/Scissors):").lower()
    computer_choice = random.choice(game)
    choice = [player_choice,computer_choice]
    return choice
def check_win(player,computer):
    print(f"You have chose {player}, Computer have chose {computer}")
    if player == computer:
        return("Its a Tie")
    elif player == "rock":
        if computer == "scissors":
            return("Player Won!")
        else:
         return("Computer Won!")
    elif player == "paper":
        if computer == "rock":
            return("Player Won!")
        else:
         return("Computer Won!")      
    elif player == "scissors":
        if computer == "paper":
            return("Player Won!")
        else:
         return("Computer Won!")
while(True):
   ch = get_choices()
   player = ch[0]
   computer = ch[1]
   print(check_win(player,computer))
   a = input("Do you want to continue (Y/N):")
   if a == 'N' or a == 'n':
      break
import sys
import random
from enum import Enum

game_count=0
def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    
    print("")
    playerchoice = input(
        "Enter...\n1 for ROCK,\n2 for PAPER, or \n3 for SCISSORS:\n\n")
    
    if playerchoice not in ["1","2","3",]:
        print ("You must enter 1, 2, or 3.")
        return play_rps()
    
    player = int(playerchoice)

    
    computerchoice = random.choice("123")

    computer = int(computerchoice)


    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + "!")
    print("I chose " + str(RPS(computer)).replace('RPS.', '') + "!\n")


    if player == 1 and computer == 3:
        print("🎊😒 You win!\nI will beat you next time!")

    elif player == 2 and computer == 1:
        print("🎊😒 You win!\nI will beat you next time!") 
        
    
        

    elif player == 3 and computer == 2:
        print("🎊😒 You win!\nI will beat you next time!")
        
        
    elif player == computer:
        print("😑 Its a tie!")
        
        
    else:
        print("🎉😼 I WIN!\nBWAHAHAHAHHAHA!")
        
        global game_count
        game_count +=1
        print("\nGame count : "+str(game_count))
        print("\nPlay Again? ")
        
        while True:
            playagain = input("\nY for yes or \nQ for Quit\n")
            if playagain.lower() not in ["y", "q"]:
              continue
            else:
                break
        
        if playagain.lower()=="y":
            return play_rps()
        else:
            print("🎊🎊")
            print("Thank you for playing!\n")
                   
        
play_rps()
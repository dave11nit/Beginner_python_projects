# this is a rock paper scissor program
# this is the third out of 12 projects
'''
in rock paper scissors a scissor beats paper, rock beats scissors and 
paper beats rocks.
The user will choose anyone of the three choices
Then the computer will choose 
And who so ever wins will be represented
'''
import random

def play():
    player = input("Choose 'R' for Rock 'P' for Paper and 'S' for scissors, Whats your choice??").lower()
    computer =  random.choice(['r','p','s'])

    if player == computer:
        return "It's a Tie"

    # r > s, s > p, p > r
    if is_win(player, computer):
        return "You Win!"

    # if none of the above two conditions agree then you
    # have surely lost
    return 'You Lose:('

def is_win(player, computer):
    # return True if the player has won
    if(player == 'r' and computer == 's') or (player == 's' and computer == 'p') and (player == 'p' and computer == 's'):
        return True
    else:
        return False


print(play())
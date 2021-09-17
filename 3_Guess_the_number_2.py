# this project is just the opposite of the 2_Guess_the_number 
# in it we will give the random number and computer will guess it
# we will tell if the guessed number is too high or low
import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # guess could have been equal to high because both of them are the same

        feedback = input(f"Is {guess} to high(H), too low(L) or is it correct(C)??").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        
    print(f"Yoohoo the computer has guess your number {guess} right!")

computer_guess(10)
# 2 out of 12 projects 
# this is a guessing game program
''' 1.computer chooses a random number
2. We need to guess that number 
3. If the number is right then print correct 
4. If the number is high then print "guess low"
5. If the number is low then print "guess high"
6. Loop it untill the user guesses the correct number.
'''
import random

def guess(x):
    random_number = random.randint(1,x)
    # lets initialize guess
    guess = 0
    # since the range of the random number is between 1 and x therefore it will not 
    # be equal to x in the first try
    while guess != random_number:
        guess = int(input(f"Guess a random number between 1 and {x}: "))
        if guess > random_number:
            print("Sorry the number is too high, guess a smaller number.")
        elif guess < random_number:
            print("Sorry the number is too low, guess a higher number.")

    print("Hooreh! You guessed the right number!")

if __name__ == "__main__":
    x = int(input("Enter the range of the number: "))
    guess(x)
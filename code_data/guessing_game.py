
from random import randint

def guess(attempts,numrange):
    number = randint(1,numrange)
    print("Welcome! Can you guess my secret number?")

    while attempts > 0:
        print("You have", attempts, "remaining")
        
        guess = input("Make a guess: ")
        
        if int(guess) ==  number:
            print("Well done! You got it right!")
            break
        elif int(guess) > number :
            print("Try going lower")
            attempts = attempts - 1
        elif int(guess) < number :
            print("Try going higher")
            attempts = attempts - 1 
        else :
            print("invalid input!")


    print("END-OF-GAME: thanks for playing!")

guess(2,7)
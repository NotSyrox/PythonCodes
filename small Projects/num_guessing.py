import random

ranNum = random.randint(1,100)

def guessNum():
    print("""
**************************************************
            Welcome to Number Guessing
**************************************************
        """)
    guesses = 1

    low = 1
    high = 100

    

    while True:
        
        guess = int(input(f"Guess a number between {low}-{high}: "))
        

        if guess == ranNum:
            break

        if guess > high or guess < low:
            print(f"Guess a number between {low}-{high}!")
            print("_______________________________________")
            
        elif guess > ranNum:
            if guess < high:
                high = guess - 1
            print("Too high!")
            print("_______________________________________")
            
            guesses +=1

            continue
        elif guess < ranNum:
            if guess > low:
                low = guess + 1
            print("Too low!")
            print("_______________________________________")
            
            guesses +=1

            continue

    return guesses

game = guessNum()
print(f"You took {game} guesses!")
print()

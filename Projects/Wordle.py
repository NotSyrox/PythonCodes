import random 
from termcolor import colored


print('''
*********************************\n
        Welcome To Wordle\n
*********************************\n
''')

word_list: list[str] = ["PAPER", "PlACE", "TIGHT", "CODES", "STYLE", "GREEN"]
Word: str = random.choice(word_list).lower()

def didWin() -> bool:  
    global attempts
    attempts = 1
    while attempts <=6 :
        userGuess = input(f"{attempts}. Guess the word: ")
        if len(userGuess) != 5:
            print("The guess was not 5 letters.")
            continue
        if userGuess == Word:
            return True
        
        output:list[str] = []
        for i in range(5):
            if userGuess[i] == Word[i]:
                output.append(colored(userGuess[i], "green"))
            elif userGuess[i] in Word:
                output.append(colored(userGuess[i], "yellow"))
            else:
                output.append(userGuess[i])
        print("".join(output))
        attempts+=1
    return False

result: bool = didWin()

if result:
    print("Yay! You won!")
    print(f"You took {attempts} attempts.")
if not result:
    print("You Lost!")
    print(f"The word was {Word.upper()}.")
import random
from art import logo

hard=5
easy=10

def play_game(turn):
    number=random.randint(1,100)
    while turn!=0:
        print(f"You have {turn} attempts left")
        guess=int(input("Make your guess:"))
        if guess==number:
            print(f"You got it, the number was {number}")
            return
        else:
            if guess<number:
                print("Too Low!\n")
            else:
                print("Too High!\n")
            turn-=1
    print("You have run out of guesses, You lost!!")
# started here  
print(logo)      
print("Welcome to number guessing game \nGuess number b/w 1 and 100")
difficulty=input("Choose difficulty level easy or hard:").lower()

if difficulty=="hard":
    play_game(hard)
elif difficulty=="easy":
    play_game(easy)
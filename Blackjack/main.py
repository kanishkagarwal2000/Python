############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
from art import logo
import sys, subprocess

def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def clear():
    subprocess.run("cls", shell=True)
def calculate(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards)==21 and len(cards)==2: #blackjack
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(c_score, p_score):
    if c_score==p_score:
        print("Draw")
    elif p_score==0:
        print("Won with a BlackJack!!!")
    elif c_score==0:
        print("You lost!! opponent has blackjack")
    elif p_score>21:
        print("You Lost, Busted!!")
    elif c_score>21:
        print("You Won!!  Opponent Busted")
    elif p_score>c_score:
        print("You won!!")
    else:
        print("You lost!!")

def play_game():
    print(logo)
    computer=[]
    player=[]
    is_gameover=False
    for _ in range(2):
        computer.append(deal())
        player.append(deal())
    while not is_gameover:
        computer_score= calculate(computer)
        player_score=calculate(player)
        print(f"Your cards: {player},  current score: {player_score}\n")
        print(f"Computer cards: {computer[0]}\n")
        if computer_score==0 or player_score==0 or player_score>21:
            is_gameover=True
        else:
            user_deal=input("Type 'y' to get another card, type 'n' to pass:")
            if user_deal=='y':
                player.append(deal())
            else:
                is_gameover=True
    while computer_score!=0 and computer_score<17:
        computer.append(deal())
        computer_score=calculate(computer)
    print(f"Your Final cards: {player}, final score: {player_score}\n")
    print(f"Computer Final cards: {computer}, final score: {computer_score}\n")
    compare(computer_score,player_score)
    


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()=="y":
    clear()
    play_game()

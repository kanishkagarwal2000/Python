from art import logo,vs
from game_data import data  #dictionary
import random
import subprocess
def random_option():
    return random.choice(data)
def print_format(choice):
    name=choice['name']
    description=choice['description']
    country=choice['country']
    return f"{name}, a {description}, from {country} "
def compare_followers(ch1,ch2):
    if(ch1['follower_count']>ch2['follower_count']):
        return 'a'
    return 'b'
def clear():
    subprocess.run("cls", shell=True)

def play_game():
    clear()
    print(logo)
    score=0
    game_on=True
    optA=random_option()
    optB=random_option()
    while game_on:
        optA=optB
        optB=random_option()
        while optA==optB:
            optB=random_option()
        
        print(f"Compare A:{print_format(optA)}")
        print(vs)
        print(f"Compare B:{print_format(optB)}")
        guess=input("Who has more followers? A or B :").lower()
        clear()
        print(logo)
        if compare_followers(optA,optB) == guess:
            score+=1
            print(f"You are right, Current Score:{score}")
        else:
            game_on=False
            print(f"sorry you are wrong, Final score:{score}")



# starts here            
play_game()
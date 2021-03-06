"""basic snakes and ladders game -> Manoj Pathak"""
from random import randint
import time

print("***** Snakes and Ladders Game *****")
"""creating ladder and snakes"""
ladders = {3:22,5:8,11:26,20:29}
snakes  = {27:1,19:7,21:9,17:4}
totalColumn = 30

"""Initialising players and their positions"""
players = {"player1":0,"player2":0,"player3":0,"player4":0,"player5":0}

def roll_dice(name, curPos):
    d = randint(1,6)
    print(name," is at position",curPos," and rolled :" ,d)
    d = curPos + d
    if d > totalColumn:
        return curPos
    else:
        return d

def check_for_snakes_and_ladders(n):
    if n in ladders:
        print("Got a ladder @ ", n, " moving from ",n ," -> ", ladders.get(n))
        n = ladders.get(n)
    elif n in snakes:
        print("Got a snake @ ", n, " moving from ",n ," -> ", snakes.get(n))
        n = snakes.get(n)
    return n

start = True;
while start:
    print()
    for k,v in players.items():
        newPos = roll_dice(k, v);
        newPos = check_for_snakes_and_ladders(newPos)
        players[k] = newPos
        time.sleep(1)  
        
        if newPos ==totalColumn:
            print("***** ",k," wins!! *****")
            start=False
            break



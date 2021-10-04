#3-Guess the random no

import random

def guess():
    rnum = random.randint(0,20)
    c = 0

    while True:
        c +=1
        num=int(input())
        if num<rnum or num>rnum:
            print("wrong")
        elif num ==rnum:
            print("right")
        else:
            print("wrong input")
guess()
        

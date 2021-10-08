#2- Program to check Change

def change(bills):
    fives = 0
    tens = 0
    twenties = 0
    for i in bills:
        if i == 5:
            fives += 1
        elif i == 10:
            tens += 1
        else:
            twenties += 1
        if len(bills) > 0 and fives == 0:
            return False
        if i == 20 and tens > 0 and fives >0:
            tens -= 1
            fives -= 1
        elif i == 20 and tens == 0 and fives < 3:
            return False
        elif i == 20 and tens == 0 and fives >=3:
            fives = fives - 3
        if i == 10 and fives > 0:
            fives -= 1
        elif i == 10 and fives == 0:
            return False
    return True

bills = [5,5,5,10,20]

print(change(bills))

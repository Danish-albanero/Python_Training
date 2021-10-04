#2- Perfect No

def perfectNumber(num):
    sum = 0
    for x in range(1, num):
        if num % x == 0:
            sum += x
    if sum == num:
        return print("perfect")
    else:
        return print("not perfect")

perfectNumber(6)
perfectNumber(24)


#Python program for Tower of Hanoi
def hanoi(x):
    if x == 1:
        return 1
    else:
        return 2*hanoi(x-1) + 1

x = int(input("enter the number od disks "))

print('number of steps:', hanoi(x))

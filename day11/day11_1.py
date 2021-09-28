#1Python Program to Implement Tower of Hanoi
def hanoi(disks, s, a, target):
    if disks == 1:
        print('Move disk 1 from peg {} to peg {}.'.format(s, target))
        return
 
    hanoi(disks - 1, s, target, a)
    print('Move disk {} from peg {} to peg {}.'.format(disks, s, target))
    hanoi(disks - 1, a, s, target)
 
 
disks = int(input('number of disks: '))
hanoi(disks, 'A', 'B', 'C')

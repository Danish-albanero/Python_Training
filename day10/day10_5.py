#5-Python program to find out the average of a set of integers
c = int(input("Enter the count"))
i = 0
sum = 0
for i in range(c):
    x = int(input("Enter an integer: "))
    sum = sum + x
avg = sum/c
print(" The average is: ", avg)

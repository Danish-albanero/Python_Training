#5-Count the digits of a number
n=int(input("Enter number:"))
c=0
while(n>0):
    c+=1
    n=n//10
print("The number of digits in the number are:",c)

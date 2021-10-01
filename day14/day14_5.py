#5Program to Print Numbers in a Range (1,max) Without Using any Loops
def printno(u):
    if(u>0):
        printno(u-1)
        print(u)
upper=int(input("Enter upper limit: "))
printno(upper)

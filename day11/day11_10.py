#10Program to Create a List of Tuples with the First Element as the Number and
#Second Element as the Square of the Number

a=int(input("Enter the lower range:"))
b=int(input("Enter the upper range:"))
c=[(x,x**2) for x in range(a,b+1)]
print(c)

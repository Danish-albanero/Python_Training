#9-rogram to Take in Two Strings and
#Display the Larger String without Using Built-in Functions
s1=input("Enter first string:")
s2=input("Enter second string:")
c1=0
c2=0
for i in s1:
      c1=c1+1
for j in s2:
      c2=c2+1
if(c1<c2):
      print("Larger string is:")
      print(s2)
elif(c1==c2):
      print("Both strings are equal.")
else:
      print("Larger string is:")
      print(s1)

#9-first letter of a string
s="My name is danish"
a=True
str=""

for i in range(len(s)):
    if s[i] == " ":
        a=True
    elif s[i] != " " and a == True:
        str +=s[i]
        a= False
print(str)
        

#8-Print first letter of every word in the string


s=input()
v=True
St=""

for char in s:
    if char == " ":
        v=True
    elif char !=" " and v == True:
        St += char + " "
        v = False
print(St)

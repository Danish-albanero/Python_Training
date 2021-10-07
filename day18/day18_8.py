#8-First character of a sentence
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

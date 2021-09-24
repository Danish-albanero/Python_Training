#8-starting letter of each word
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

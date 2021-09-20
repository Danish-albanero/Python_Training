#2. longest substring

s = "abcadacc"
max1= []
li = []
li.append(s[0])

for i in range(len(s)):
    if s[i] not in li:
        li.append(s[i])

    else:
        max1.append(len(li))
        li = []
        
print(max(max1))

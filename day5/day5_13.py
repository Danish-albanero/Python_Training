
#length of last word
s="My name is danish"
i=len(s)-1
j=i
while(s[j] != " "):
    j -=1
q=s[j+1:i+1]
print(len(q))

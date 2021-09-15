s="my name is danish"
a=len(s)-1
ans=""
while(a>=0):
    while a>=0 and s[a] == " ":
        a -=1
    i=a+1
    while a>=0 and s[a] != " ":
        a -=1
    str=s[a+1:i+1]
    if len(ans) == 0:
        ans=str
    else:
        ans +=" "+str
    
    
print(ans)

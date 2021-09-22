#2- Reverse a string

def revStr (S):
    a=len(S)-1
    ans=""
    while(a>=0):
        while a>=0 and S[a] == " ":
            a -=1
        i=a+1
        while a>=0 and S[a] != " ":
            a -=1
        str=S[a+1:i+1]
        if len(ans) == 0:
            ans=str
        else:
            ans +=" "+str
    return ans

s="My name is danish"
print(revStr(s))

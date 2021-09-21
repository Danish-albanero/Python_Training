#Magical String[Duplicate Problem
def magicalString(S):
    b="abcdefghijklmnopqrstuvwxyz"
    size=len(S)
    ans=""
    for i in range(size):
        d=ord(S[i])-ord('a')
        ans+=b[25-d]
    return ans

s="danish"
print(magicalString(s))

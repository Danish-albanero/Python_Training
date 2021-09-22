#4-the penalty shootout
def penaltyscore(s):
    ans = 0
    for i in range(len(s)):
        if (s[i] == '1' and s[i-1]=='2'):
            ans +=1
    return ans
s="1012012112110"
print(penaltyscore(s))

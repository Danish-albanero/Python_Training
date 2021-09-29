#3Shortest distance to every other character from given character
def shortestdis(s,c):
    inf = [float('inf')]
    p = inf
    ans = []
    for i,j in enumerate(s):
        if s[i] == c:
            p = i
        if (p == inf):
            ans.append(inf)
        else:
            ans.append(i-p)

    p = inf
    for i in range(len(s)-1, -1, -1):
        if s[i] == c:
            p = i
        if (c != inf):
            ans[i] = min(ans[i], p-i)

    return ans
s = "loveleetcode"
c = "e"
print(shortestdis(s,c))


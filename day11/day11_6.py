#6-length of the longest valid substring

def findmax(s):
    n = len(s)
    a = []
    a.append(-1)
    r = 0

    for i in range(n):
        if s[i] == '(':
            a.append(i)
        else:
            if len(a) != 0:
                a.pop

            if len(a) !=0:
                r = max(r, i-a[len(a)-1])


            else:
                a.append(i)
    return r


s = "((()()"
print(findmax(s))

            

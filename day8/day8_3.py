#3UniquePath

def unique(a,b):
    li = [[1 for x in range(b)] for x in range(a)]
    for i in range(1,a):
        for j in range(1,b):
            li[i][j] = li[i-1][j] + li[i][j-1]
    return li[-1][-1]

a=3
b=3
print(unique(a, b))

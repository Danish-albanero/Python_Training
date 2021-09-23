#2-climb stairs


def climbcount(n):
    if n == 1 or n ==2:
        return n
    p = 1
    p1 = 2
    c = 0
    for i in range(3,n+1):
        c = p + p1
        p = p1
        p1 = c

    return c
n=5
print(climbcount(n))


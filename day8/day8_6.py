#6    *
#     ***
#     *****
n=3
for i in range(n+1):
    for j in range(n-i):
        print("",end='')

    for k in range(2*i -1):
        print("*", end = '')
    print()

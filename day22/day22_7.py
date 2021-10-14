
#7 count the zeros

def count(arr):
    c=0
    for i in arr:
        if i == 0:
            c +=1
    return c

arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
print(count(arr))



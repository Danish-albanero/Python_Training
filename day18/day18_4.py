#4 -Selection Sort in descending order
li = [4,7,1,3,22,5,3,2]

for i in range(len(li)):
    min1 = max(li[i:])
    min2 = li.index(min1)
    li[i],li[min2] = li[min2],li[i]

print(li)

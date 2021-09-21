#16 Remove elements

lis=[1,2,3,4,5,6,7]
target = 3

for i in range(len(lis)-1):
    if lis[i] == target:
        lis.remove(lis[i])

print(lis)

#1- Duplicate Zeros


li = []
n = int(input("enter no of elements"))
for i in range(n):
    a = int(input())
    li.append(a)
for i in range(len(li)):
    if li[i] == 0:
        li.insert(i+1, 0)
        break

print(li)
    

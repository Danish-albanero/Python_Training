#4-Find First and Last Position of Element in Sorted Array
list1 = [5,7,7,8,8,10]
target=int(input())
li=[] 


j=len(list1)-1
for i in range(len(list1)):
    if list1[i] == target:
        
        li.append(i)
        break

for j in range(len(list1)-1,0,-1):
    if list1[j] == target:
        
        li.append(j)
        break
print(li)

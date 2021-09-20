#merge two sorted list

list1=[1,3,5,7,9]
list2=[2,4,6,8]
arr=[]
list1_len=len(list1)
list2_len=len(list2)
i=j=k=0

while i<list1_len and j<list2_len:
    if list1[i]<=list2[j]:
        arr[k]=list1[i]
        i+=1
    else:
        arr[k]=list2[j]
        j+=1
    k+=1
while i<list1_len:
    arr[k]=list1[i]
    i+=1
    k+=1
while j<list2_len:
    arr[k]=list2[j]
    j+=1
    k+=1

for i in arr:
    print(i)



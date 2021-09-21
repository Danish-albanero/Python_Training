#6 implementing insertion sort
def Insertion_Sort(arr):
    n =len(arr)
    for i in range(1,n):
       k = arr[i]
       j=i-1 
       while j >= 0 and k < arr[j]:
           arr[j+1] = arr[j]
           j -=1
       arr[j+1] = k
    return arr
li= [5,2,7,1,4,8]
a=[]
a =Insertion_Sort(li)
print(a)

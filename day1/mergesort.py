def mergesort(arr):
    if len(arr)<=1:
        return
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    mergesort(left)
    mergesort(right)

    merge(left,right,arr)

def merge(a,b,arr):
    a_len=len(a)
    b_len=len(b)
    i=j=k=0

    while i<a_len and j<b_len:
        if a[i]<=b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while i<a_len:
        arr[k]=a[i]
        i+=1
        k+=1
    while j<b_len:
        arr[k]=b[j]
        j+=1
        k+=1


arr=[2,4,3,2,4,3,21,5,7,4]
mergesort(arr)
print(arr)

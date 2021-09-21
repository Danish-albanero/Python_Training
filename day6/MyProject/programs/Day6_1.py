#Search insert position

def binary(arr,low, high, target):
    if(low<high):
        mid = (low + high)//2
        if arr[mid] == target:
            return 1
        elif target< arr[mid]:
            return binary(arr,low,mid-1,target)
        elif target > arr[mid]:
            return binary(arr,mid+1,high,target)
    else:
        return -1
arr=[1,2,3,4,6,7,8,9]
k=int(input())
low=0
high=len(arr)-1
a=binary(arr,low,high,k)
if(a == 1):
    print("found")
else:
    for i in range(len(arr)):
        if arr[i]<k:
            continue
        else:
            print("if target exist then its index would be: ",i)
            break
              






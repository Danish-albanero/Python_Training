#8Peak element

def peak(arr,n):
    if n is 1:
        return 0
    for i in range(n):
        if i==0 and arr[1]<arr[0]:
            return 0
        elif  i==n-1 and arr[n-2]<arr[n-1]:
            return n-1
        elif arr[i-1]<arr[i] and arr[i]>arr[i+1]:
            return i

n=3
arr = [1,2,3]
print(peak(arr,n))

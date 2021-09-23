#highest subarray sum
def MaxSubSum(arr):
    max=0
    cur=0
    for i in range(len(arr)):
        cur = cur + arr[i]
        if(cur > max):
            max = cur
        if(cur<0):
            cur =0
    return max
arr=[5,-3,-2,6,1]
a=MaxSubSum(arr)
print(a)

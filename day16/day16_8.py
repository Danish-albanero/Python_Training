#8maximum subarray sum with one deletion
def maximumSum(arr):
    max1 = max2 = res = arr[0]
    for n in arr[1:]:
        max1 = max(max1 + n, n, max2)
        max2 = max(max2 + n, n)
        res = max(max1, res)
    return res
arr = [1, -2, 1, 3, 0, -2, 7]
print(maximumSum(arr))

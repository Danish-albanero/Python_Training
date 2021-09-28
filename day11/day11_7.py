#7-Search insert position of K in a sorted array


def find(arr, n, k):
    for i in range(n):
        if arr[i] == k:
            return i
        elif arr[i] > k:
            return i
    return n

arr = [1,3,5,6]
n = len(arr)
k = 4
print(find(arr, n, k))

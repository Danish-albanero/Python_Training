#2-Program to Implement Binary Search without Recursion
def binary_search(li, key):
    s = 0
    e = len(li)
    while s < e:
        mid = (s + e)//2
        if li[mid] > key:
            e = mid
        elif li[mid] < key:
            s = mid + 1
        else:
            return mid
    return -1
 
 
li= [1,2,3,4,5,6,7,8,9]
key = int(input('The number to search for: '))
 
index = binary_search(li, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))

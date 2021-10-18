#1Split array in three equal sum subarrays
def findSplit(arr, n):
    presum = 0
    index = -1
    index1 = -1

    S = arr[0]
    for i in range(1, n):
        S += arr[i]


    if(S%3 != 0):
        return 0

    S1 = S/3
    S2 = 2 *S1

    for i in range(0,n):
        presum += arr[i]

        if(presum == S1 and index == -1):
            index = i

        elif(presum == S2 and index != -1):
            index1 = i

            break

    if(index != -1 and index1 != -1):
        print("({},{})".format(index, index1))
        return 1
arr = [1,3,4,0,4]
n = len(arr)
if(findSplit(arr, n) == 0):
    print("-1")

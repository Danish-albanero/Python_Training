#5 Height checker
def heightCheck(heights):
    ans = 0
    x = sorted(heights)
    y = heights
    for i in range(len(x)):
        if x[i]!=y[i]:
            ans+=1
    return ans
li = [1,2,4,2,1,3]
print(heightCheck(li))

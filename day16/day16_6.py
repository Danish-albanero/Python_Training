#6-Distribute Candies to People
def distributeCandies(candies, num_people):
    res = [0 for i in range(num_people)]
    index = 0
    while candies>0:
        res[index%num_people] += min(candies,index+1)
        candies-=(index+1)
        index+=1
    return res

print(distributeCandies(8, 3))


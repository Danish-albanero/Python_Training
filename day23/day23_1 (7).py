#7best-sightseeing-pair
def maxScoreSightseeingPair(A):
    result, curr = 0, 0
    for x in A:
        result = max(result, curr+x)
        curr = max(curr, x)-1
    return result

A = [1,2,3,4,5,6,6]
print(maxScoreSightseeingPair(A))

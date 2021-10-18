#4Find the Town Judge
def findJudge(N, trust):
    degrees = [0]*N
    for i, j in trust:
        degrees[i-1] -= 1
        degrees[j-1] += 1
    for i in range(len(degrees)):
        if degrees[i] == N-1:
            return i+1
    return -1


N= 3
trust = [[1,3],[2,3]]
print(findJudge(N, trust))

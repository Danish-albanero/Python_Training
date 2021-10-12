#2Maximize Sum Of Array After K Negations
def SumAfterNegation(a,k):
    a.sort()
    for i in range(len(a)):
        if a[i]<0:
            a[i] = -a[i]
            k -= 1
        if k == 0:
            break
    if k%2:
        smallest_posi = a[0]
        for i in range(1,len(a)):
            if a[i]>=0:
                smallest_posi = min(smallest_posi,a[i])
                return sum(a) - (2*smallest_posi)
            else:
                return sum(a)
a = [3,-1,0,2]
k = 3
print(SumAfterNegation(a,k))
            

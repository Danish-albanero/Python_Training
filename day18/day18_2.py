#2-Armstrong number

def armstrong(n):
    p=len(str(n))
    ans = n
    sum = 0
    while(n>0):
        a=n%10
        sum += a ** p
        n=n//10
    if sum == ans:
        print("armstrong")
    else:
        print("not armstrong")

    

n=153
armstrong(n)

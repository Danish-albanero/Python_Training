#6 sum of digit recursively

l=[]
def sum_digits(b):
    if(b==0):
        return l
    d=b%10
    l.append(d)
    sum_digits(b//10)
n=int(input("Enter a number: "))
sum_digits(n)
print(sum(l))

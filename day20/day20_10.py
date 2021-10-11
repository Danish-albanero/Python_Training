#10Swap alternate elements
n=int(input())
li=[]
for i in range(n):
    li.append(int(input()))
i=0

while(i<n-1):
    temp=li[i]
    li[i]=li[i+1]
    li[i+1]=temp
    i+=2
print(li)

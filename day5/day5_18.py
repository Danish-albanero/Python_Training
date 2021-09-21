#18display largest name
def longestSring(name, n):
    max=0
    for i in range(1,n):
        if len(name[i]) > len(name[max]):
            max = i


    return name[max]

name = []
n=5
for i in range(n-1):
    name[i]=input()

print(longestString(name,n))
    
        

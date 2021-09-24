#2 print pattern
#1
#22
#333
#4444
#55555
'''
n=5

for i in range(1,n+1):
    for j in range(i):
        print(i, end="")
    print()
'''
        
#1
#12
#123
#1234
#12345

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    print()
        

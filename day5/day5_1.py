#1-Two Sum

a = [3,2,4]
#[2, 7, 11, 15]
target = 6

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i]+a[j] == target:
            print(i,j)

#8-BubbleSort

def bubble(li):
    for i in range(len(li)):
        for j in range(len(li)-1,i,-1):
            if li[j]<li[j-1]:
                li[j],li[j-1]= li[j-1],li[j]

    return li

li = [3,5,1,5,22,1,4,5,9]
print(bubble(li))

#4Write a program to generate and print another tuple
#whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in range(len(tp)):
	if tp[i]%2==0:
		li.append(tp[i])

tp2=tuple(li)
print(tp2)

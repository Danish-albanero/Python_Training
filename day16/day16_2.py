#2- Occurrences After Bigram

text = "alice is a good girl she is a good student"
first = "a"
second = "good"
li = []
x = text.split()


for i in range(len(x)):
    if x[i] == first and x[i+1] == second:
        li.append(x[i+2])

print(li)
        

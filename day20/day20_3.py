#3-Program to Count the Occurrences of a Word in a Text File
fn = input("Enter file name: ")
word=input("Enter word to be searched:")
k = 0
 
with open(fn, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==word):
                k=k+1
print("Occurrences of the word:")
print(k)

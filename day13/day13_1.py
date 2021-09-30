#1-Check if a string is Isogram or not

def isogram(word):

    word1 = word.lower()

    li = []


    for item in word1:
        if item.isalpha():
            if item in li:
                return False
            li.append(item)
    return True

a = "danish"
print(isogram(a))

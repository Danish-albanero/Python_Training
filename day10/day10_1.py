#1-Count the number of strings where the string length is 2 or
#more and the first and last character are same from a given list of strings


def wordmatch(words):
    c = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            c +=1
    return c
li = ['abc', 'xyz', 'aba', '1221']
print(wordmatch(li))

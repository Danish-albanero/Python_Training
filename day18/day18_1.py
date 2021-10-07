#1- count character frequency

def charFrequency(n):
    
    n = n.lower()
    dict = {}
    for char in n:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


n = str(input('Enter a string: '))
print(charFrequency(n))

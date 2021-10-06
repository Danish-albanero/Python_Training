#9-program to print even length words in a string

def evenword(s):

    s = s.split(' ')

    for item in s:
        if len(item)%2 == 0:
            print(item)


s= "My name is danish"
evenword(s)

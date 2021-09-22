#3-count of camel case character
def Camel(s):
    r = 0
    for i in s:
        if i>='A' and i<='Z':
            r +=1

    return r
s="asddasdASDASDAsasa"
print(Camel(s))

#6-Count Substring

def count(s):
    c = 0
    for i in s:
        if i == '1':
            c +=1
    return(c*(c-1))//2

s = "10101"
print(count(s))

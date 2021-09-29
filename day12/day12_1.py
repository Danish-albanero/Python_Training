#1- Buddy String

def buddy(a,b):
    if len(a) != len(b):
        return False
    elif sorted(a) != sorted(b):
        return False
    else:
        c = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                c +=1
                if c == 3:
                    return False
        return True
a="ba"
b="ab"
print(buddy(a,b))

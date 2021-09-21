#14 reverse Interger

def reverse(x):
    rev = 0
    while(x!=0):
        rev = rev*10 +x%10
        x=x//10
    return rev

x=123
print(reverse(x))

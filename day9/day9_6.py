#6 reverse as string using recursion
def reverse(str):
    if len(str)  == 1:
        return str
    else:
        return reverse(str[1:])+str[0]
str=input()
str1 = reverse(str)
print(str1)

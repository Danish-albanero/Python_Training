
#Sum of numbers in string
def findSum(s):
    temp=0
    sum =0

    for item in s:
        if (item.isdigit()):
            temp +=(item)

        else:
            sum += int(temp)

            temp = "0"

    return sum +int(temp)
s="1bc23"
print(findSum(s))

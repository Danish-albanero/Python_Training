#FizzBuzz

n=20
for i in range(n):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3 == 0:
        print("fizz")
    elif i%5 == 0:
        print("buzz")

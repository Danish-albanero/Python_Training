''''
--------------------------------------------------------------------
handling different question
try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)
    
except ValueError as e:
    print("Please Enter a valid value") 

except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0") 

print("Thanks for using this code!")
---------------------------------------------------------------------
'''
'''
raising exception

def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("invalid number")

a = increment('df364')
print(a)
-----------------------------------------------------
'''
'''
try- else
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
else:
    print("successful")
------------------------------------------------------------

'''
'''
try-except-finally
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    
finally:
    print("We are done")

print("Thanks")
----------------------------------------------------------------
'''



























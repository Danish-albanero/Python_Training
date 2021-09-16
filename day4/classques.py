'''Create a Cricle class and intialize it with radius.
Make two methods getArea and getCircumference inside this class.


class Circle:
    def __init__(self, r):
        self.r =r
    def getArea(self):
        print(3.14 *(self.r ** 2))
    def getCircumference(self):
        print(2*(3.14*self.r))
Circleobj= Circle(5)
Circleobj.getArea()
Circleobj.getCircumference()
-------------------------------------------------------------------------
'''
'''
Create methods for the Calculator class that can do the following:

Add two numbers.
Subtract two numbers.
Multiply two numbers.
Divide two numbers.



class Calc:
        def __init__(self, a , b):
                self.a = a
                self.b = b
        def addnum(self):
                print(self.a + self.b)
        def addsub(self):
                print(self.a - self.b)
        def addmul(self):
                print(self.a * self.b)
        def adddiv(self):
                print(self.a / self.b)
                
c= Calc(10,5)
c.addnum()
c.addsub()
c.addmul()
c.adddiv()
-------------------------------------------------------------------------------
'''
'''
class Person:
        def common_task(self):
                print("work")
                print("earn")
                print("spend")
class Employee(Person):
        def __init__(self, fname, lname, sal):
                self.fname = fname
                self.lname = lname
                self.sal = sal
        def work(self):
                super().common_task()
                print(f"{self.fname}{self.lname}cal")
                print("task")
                print("report")
                print("email")
e=Employee("danish","ali",41233)
e.work()
----------------------------------------------------------------------------
''''
                
        




































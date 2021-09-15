class Employee:
    def __init__(self, name, id, sal):
        self.name = name
        self.id   = id
        self.sal  = sal
    def print(self):
        print(f"Employee:{self.name} with id:{self.id} have salary:{self.sal}")
ee=Employee("Danish","1","12222")
e2=Employee("qwweq","2","1222332")
ee.print()
e2.print()

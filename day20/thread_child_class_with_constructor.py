from threading import *
class Mythread(Thread):
    def __init__(self, a):
        Thread.__init__(self)
        print("child", a)


t = Mythread(10)
t.start()
print("main")
from threading import Thread, current_thread
from time import sleep

def disp():
    print("child thread :", current_thread().getName())
    current_thread().setName('Thread demo')
    print("child thread :", current_thread().getName())
    sleep(0.2)

t = Thread(target=disp)
t.start()
t.join()

print("main :", current_thread().getName())
current_thread().setName('Main demo')
print("main thread :", current_thread().getName())

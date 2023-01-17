from time import sleep
import threading


def foo():
    for x in range(5):
        sleep(1)
        print(x)

def bar():
    for x in range(5):
        sleep(.5)
        print(x)

# While we can open 2 OS threads.
# The python interpreter can only process from one thread at a time. RE: GIL.
x = threading.Thread(target=foo)
y = threading.Thread(target=bar)
x.start()
y.start()
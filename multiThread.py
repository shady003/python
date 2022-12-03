from threading import *
from time import *


class thr1(Thread):
    def run(self):
        for i in range(3):
            print('thr1')
            sleep(2)


class thr2(Thread):
    def run(self):
        for i in range(3):
            print('thr2')
            sleep(2)


t1 = thr1()
t2 = thr2()

t1.start()
sleep(.2)
t2.start()

t1.join()
t2.join()

print('code Ended')

from threading import *
import random
import time


class Worker(Thread):
    def __init__(self, index, group=None, target=None, name=None, args=None, kwargs=None, *, daemon=None) -> None:
        super().__init__(group=group, target=target, name=name,
                         args=args, kwargs=kwargs, daemon=daemon)
        self.index = index

    def run(self) -> None:
        print('starting: Thread {}'.format(self.index))
        timer = random.choice(range(5))
        print('Thread {} is sleeping for {} seconds'.format(self.index, timer))
        time.sleep(timer)
        print('Thread {} is closing'.format(self.index))


for i in range(5):
    t1 = Worker(i)
    t1.start()

print("main thread finished")

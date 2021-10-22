import threading
import time
import random


def threadFuction(index):

    print('starting: Thread {}'.format(index))
    timer = random.choice(range(2))
    print('Thread {} is sleeping for {} seconds'.format(index, timer))
    time.sleep(timer)
    print('Thread {} is closing'.format(index))


threads = []

for i in range(3):
    th = threading.Thread(target=threadFuction, args=(i,), daemon=True)
    th.start()
    threads.append(th)

# for index, th in enumerate(threads):
#     th.join()
#     print("Thread {} fininshed Successfully!".format(index))

print("Main thread Working")

"""
1) On Linux and probably on Windows too, when the main thread exits, its child threads are terminated. 
How does this affect the mentioned behavior in question? If the main thread was able to exit during its 
time slice, before being context switched with another thread, no fatal error occurs as all threads get 
terminated. Nothing guarantees however, that the main thread will exit as soon as it starts.

2) The fatal error takes place between the finalization process (shutdown) of the interpreter and the 
read, write, or flush call and possibly other operations on the Buffered* object. The finalization process 
acquires the lock of the those objects, any write for example to the BufferedWriter object results in 
Fatal Python error.

"""

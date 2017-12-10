import random
import threading
import time


THREADS = 5


def worker(number):
    sleeping_time = random.randrange(1, 10)
    time.sleep(sleeping_time)
    print("I'm worker {} and I slept {} seconds".format(number, sleeping_time))


for thread_number in range(THREADS):
    t = threading.Thread(target=worker, args=(thread_number,))
    t.start()



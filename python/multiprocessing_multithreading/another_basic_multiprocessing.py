import random
import multiprocessing
import time


PROCESSES = 5


def worker(number):
    sleeping_time = random.randrange(1, 10)
    time.sleep(sleeping_time)
    print("I'm worker {} and I slept {} seconds".format(number, sleeping_time))


for process_number in range(PROCESSES):
    process = multiprocessing.Process(target=worker, args=(process_number,))
    process.start()

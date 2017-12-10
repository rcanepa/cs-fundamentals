import threading
import time
import random

SLEEP = True
counter = 0


# Making race conditions visible by introducing sleep time periods
def sleep_for_a_while():
    if SLEEP:
        time.sleep(random.random())


def worker():
    global counter

    sleep_for_a_while()
    old_counter = counter
    sleep_for_a_while()
    counter = old_counter + 1
    sleep_for_a_while()
    print("Counter: %d" % counter, end='')
    sleep_for_a_while()
    print()
    sleep_for_a_while()
    print("---------------------", end='')
    sleep_for_a_while()
    print()


print("Work started!")
sleep_for_a_while()
for t in range(10):
    threading.Thread(target=worker).start()
    sleep_for_a_while()
sleep_for_a_while()
print("Work finished!")
sleep_for_a_while()
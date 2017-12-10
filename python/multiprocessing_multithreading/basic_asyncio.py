import asyncio
import datetime
import random


async def my_sleep_func(who_is_sleeping):
    sleep_time = random.randint(0, 5)
    print("\t-> Loop {} is going to sleep for {} seconds".format(who_is_sleeping, sleep_time))
    await asyncio.sleep(sleep_time)


async def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func(num)

loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()

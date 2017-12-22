import time


def average(numbers):
    return sum(numbers) / len(numbers)


def timedcall(fn, *args):
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1 - t0, result


def timedcalls(n, fn, *args):
    times = [timedcall(fn, *args)[0] for _ in range(n)]
    return min(times), average(times), max(times)


if __name__ == "__main__":
    fn = sum
    print(timedcalls(1000, fn, list(range(100000))))

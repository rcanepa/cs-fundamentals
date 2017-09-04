import random


def is_sorted(array):
    return array == sorted(array)


def create_random_array(size):
    return [random.randrange(0, size * 10, 1) for x in range(size)]

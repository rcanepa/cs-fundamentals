import time
from utils.arrays import create_random_array


def partition(array, low, high):
    moving_target = low + 1
    index = moving_target
    while index <= high:
        if array[index] < array[low]:
            array[index], array[moving_target] = array[moving_target], array[index]
            moving_target += 1
        index += 1
    moving_target -= 1
    array[low], array[moving_target] = array[moving_target], array[low]
    return moving_target


def sort(array, low, high):
    if low >= high:
        return array
    half = partition(array, low, high)
    sort(array, low, half - 1)
    sort(array, half + 1, high)
    return array


def quicksort(array):
    sort(array, 0, len(array) - 1)
    return array


def is_sorted(array):
    return array == sorted(array)


if __name__ == '__main__':
    size = 10000
    random_list = create_random_array(size)
    t0 = time.time()
    sorted_list = quicksort(random_list)
    t1 = time.time()
    if not is_sorted(sorted_list):
        raise Exception('The array was not correctly sorted.')
    if size < 20:
        print('Unsorted array   =>    {}'.format(random_list))
        print('Sorted array     =>    {}'.format(sorted_list))
    print('Took {:.3f}ms to sort {} elements.'.format((t1 - t0) * 1000, size))

import random
import time

from utils.arrays import create_random_array, is_sorted


def merge(leftArray, rightArray):
    sorted_array = []
    lp, rp = 0, 0
    while (lp < len(leftArray) and rp < len(rightArray)):
        if (leftArray[lp] <= rightArray[rp]):
            sorted_array.append(leftArray[lp])
            lp += 1
        else:
            sorted_array.append(rightArray[rp])
            rp += 1

    while (lp < len(leftArray)):
        sorted_array.append(leftArray[lp])
        lp += 1

    while (rp < len(rightArray)):
        sorted_array.append(rightArray[rp])
        rp += 1

    return sorted_array


def mergesort(array):
    array_length = len(array)
    if (array_length == 0 or array_length == 1):
        return array

    half = array_length // 2
    left = mergesort(array[0:half])
    right = mergesort(array[half:array_length])

    return merge(left, right)


if __name__ == '__main__':
    size = 10000
    random_list = create_random_array(size)
    t0 = time.time()
    sorted_list = mergesort(random_list)
    t1 = time.time()
    if (not is_sorted(sorted_list)):
        raise Exception('The array was not correctly sorted.')
    if (size < 20):
        print('Unsorted array   =>    {}'.format(random_list))
        print('Sorted array     =>    {}'.format(sorted_list))
    print('Took {:.3f}ms to sort {} elements.'.format((t1 - t0) * 1000, size))

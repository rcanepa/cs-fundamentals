import random


def partition(array, low, high):
    moving_target = low + 1
    index = moving_target
    while index <= high:
        if (array[index] < array[low]):
            array[index], array[moving_target] = array[moving_target], array[index]
            moving_target += 1
        index += 1
    moving_target -= 1
    array[low], array[moving_target] = array[moving_target], array[low]
    return moving_target


def sort(array, low, high):
    if (low >= high):
        return array
    half = partition(array, low, high)
    sort(array, low, half - 1)
    sort(array, half + 1, high)
    return array


def quicksort(source_array):
    array = source_array.copy()  #  don't mutate the original array
    sort(array, 0, len(array) - 1)
    return array


def is_sorted(array):
    return array == sorted(array)


def create_random_array(size):
    return [random.randrange(0, size * 10, 1) for x in range(size)]


if __name__ == '__main__':
    random_list = create_random_array(15)
    sorted_list = quicksort(random_list)
    print('Unsorted array   =>    {}'.format(random_list))
    print('Sorted array     =>    {}'.format(sorted_list))
    print('Is the result array sorted? => {}'.format(is_sorted(sorted_list)))

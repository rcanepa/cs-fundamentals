""" Heap sort. A O(n * log(n)) operation to sort
a list in increasing order. It's based on a MinHeap
implementation (Priority Queue).
"""
from heaps.min_heap import MinHeap
from utils.arrays import create_random_array


def heap_sort(source_list=None):
    if isinstance(source_list, list):
        sorted_data = []
        # Building the heap is an O(n * log(n)) operation, because inserting
        # an element in the heap is an O(log(n)) operation, and this operation
        # must be executed n times (one for every element on the source list).
        heap = MinHeap(source_list)
        while heap.size > 0:
            sorted_data.append(heap.remove())
        return sorted_data
    else:
        raise Exception("You must provide a list in order to execute this process.")


if __name__ == '__main__':
    random_array = create_random_array(100)
    sorted_array = heap_sort(random_array)

    # Check the array is sorted in increasing order.
    index = 0
    for current_value in sorted_array[1:]:
        previous_value = sorted_array[index]
        if current_value < previous_value:
            raise Exception(
                "The array isn't sorted. index {} has value {}, and index {} has value {}".format(
                    index,
                    previous_value,
                    index + 1,
                    current_value
                )
            )
        index += 1
    print("The array was correctly sorted.")

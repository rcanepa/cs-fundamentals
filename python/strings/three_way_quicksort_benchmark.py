"""
Benchmarks (string size = 10):
- Took 6.607ms to sort 1000 elements.
- Took 86.542ms to sort 10000 elements.
- Took 1091.928ms to sort 100000 elements.
"""
import time

from strings.three_way_quicksort import sort
from utils.arrays import is_sorted
from utils.strings import generate_random_string


if __name__ == "__main__":
    string_size = 10
    number_of_strings = 1000
    random_strings = [generate_random_string(string_size) for _ in range(number_of_strings)]

    t0 = time.time()
    sort(random_strings)
    t1 = time.time()

    if not is_sorted(random_strings):
        raise Exception('The array was not correctly sorted.')
    print('Took {:.3f}ms to sort {} elements.'.format((t1 - t0) * 1000, number_of_strings))

    # with open("msd_string_sort_usage_data.txt", "w") as f:
    #    for string in sorted_strings:
    #        f.write(string + "\n")

"""Key-indexed counting sorting algorithm.
Extremely effective sorting algorithm for data in which the sorting keys
are small integers.

Characteristics:
    - Stable (preserves original order).
    - Linear time O(n) when R is within a constant factor o N and when keys
      are integers between 0 and R - 1.

Applications:
    - Sort by area code.
    - Sort by string first letter.
    - Sort by age.
"""
from collections import namedtuple


def _initialize_list(size, default_value):
    return [default_value] * size


def key_indexed_counting_sort(data, sorting_field):
    # Radix: number of different possible integers.
    r = max([getattr(s, sorting_field) for s in data]) + 1

    # Initialize a list with max(section) + 2 zeros.
    count = _initialize_list(r + 1, 0)

    # Step 1: Compute section frequencies.
    # Calculate how many students are per section.
    for s in data:
        count[getattr(s, sorting_field) + 1] += 1

    # print(count)
    # => [0, 0, 3, 5, 6, 6]
    #           ^ section 1 has 3 students
    #              ^ section 2 has 5 students

    # Step 2: Transform frequencies to indices.
    # Now `count` keeps track of the starting position of the students for
    # every section.
    for index in range(r):
        count[index + 1] += count[index]
    # print(count)
    # => [0, 0, 3, 8, 14, 20]
    #        ^ students from section 1 start from position 0
    #           ^ students from section 2 start from position 3

    # Before starting step 3 (distributing the data).
    # |-------------|-------------|-----------------|-------------|
    #  ^             ^             ^      ...        ^
    # count[0]    count[1]     count[2]   ...    count[R - 1]

    # During step 3 (the starting point of each section moves to the left as the students
    # are located in the sorted list.)
    # |0------------|11111--------|2---------------|R-1R-1R-1-----|
    #   ^                 ^         ^      ...               ^
    # count[0]    count[1]     count[2]   ...    count[R - 1]

    # When the process is finished and all students are in their final position.
    # |0000000000000|1111111111111|2222222222222222|R-1R-1R-1R-1R-1|
    #                ^             ^      ...       ^               ^
    #              count[0]    count[1]          count[2]  ...  count[R - 1]

    students_sorted_by_section = _initialize_list(len(data), None)

    # Step 3: Distribute data.
    # Sort students by section according to the count list.
    for index, student in enumerate(data):
        # Find the sorted position of the current students.
        student_starting_position = count[getattr(data[index], sorting_field)]

        # Increment the starting position of the student's section.
        count[getattr(data[index], sorting_field)] += 1
        students_sorted_by_section[student_starting_position] = data[index]

    return students_sorted_by_section


if __name__ == "__main__":
    Student = namedtuple("Student", ["name", "section"])
    students = [
        Student("Anderson", 2),
        Student("Brown", 3),
        Student("Davis", 3),
        Student("Garcia", 4),
        Student("Harris", 1),
        Student("Jackson", 3),
        Student("Johnson", 4),
        Student("Jones", 3),
        Student("Martin", 1),
        Student("Martinez", 2),
        Student("Miller", 2),
        Student("Moore", 1),
        Student("Robinson", 2),
        Student("Smith", 4),
        Student("Taylor", 3),
        Student("Thomas", 4),
        Student("Thompson", 4),
        Student("White", 2),
        Student("Williams", 3),
        Student("Wilson", 4)
    ]
    # In this case, R = 5 (0, 1, 2, 3, 4).
    # `count` goes from 0 to 6, because position number 0 isn't used.
    # So, the frequency of number 4 is store in count[4 + 1] (last available position).

    sorted_data = key_indexed_counting_sort(students, "section")
    print(sorted_data)

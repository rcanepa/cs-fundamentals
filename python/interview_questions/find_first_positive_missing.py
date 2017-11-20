"""Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space."""


def first_missing_positive(nums):
    if not nums:
        return 1

    n = len(nums)

    if n == 1:
        return 1 if nums[0] != 1 else 2

    for i in range(n):
        while n >= nums[i] > 0 and nums[i] != nums[nums[i] - 1]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == "__main__":
    test_cases = [
        ([3, 4, -1, 1], 2),
        ([1, 2, 5, 4], 3),
        ([10, 2, 5, 4], 1),
        ([2, 3], 1),
        ([2], 1),
        ([1], 2),
        ([], 1),
        ([3], 1),
        ([-20, 1, 3, 20, 2, -4, -2], 4)
    ]
    for numbers, expected_result in test_cases:
        assert first_missing_positive(numbers) == expected_result

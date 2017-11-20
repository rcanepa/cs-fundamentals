"""Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


from heapq import heappop, heappush


def longest_substring(string):
    if len(string) <= 1:
        return len(string)

    min_heap = []
    char_tracker = {}
    longest_size = 0
    # TC: O(N * log(M)), N = len(string) and M = len(min_heap)
    for index, char in enumerate(string):  # O(N), where N = len(string)
        if char in char_tracker:
            longest_size = max(longest_size, len(min_heap))
            while True:
                position, min_element = heappop(min_heap)  # O(log(M))
                char_tracker.pop(min_element)
                if min_element == char:
                    break
        heappush(min_heap, (index, char))  # O(log(M)), where M = len(min_heap)
        char_tracker[char] = index  # O(1)

    return max(longest_size, len(min_heap))


def longest_substring_version2(string):
    n = len(string)
    char_tracker = {}
    longest_size = i = j = 0
    # TC: O(N + N) ~ O(N), where N = len(string)
    # SC: O(min(N, M)), where M = len(char_tracker.keys())
    while i < n and j < n:
        if string[i] not in char_tracker:
            char_tracker[string[i]] = i
            i += 1
            longest_size = max(longest_size, i - j)
        else:
            char_tracker.pop(string[j])
            j += 1
    return longest_size


def longest_substring_version3(string):
    n = len(string)
    char_tracker = {}
    start_window_index = 0
    longest_size = 0
    for end_window_index in range(n):
        if string[end_window_index] in char_tracker:
            start_window_index = max(start_window_index, char_tracker[string[end_window_index]] + 1)
        longest_size = max(longest_size, end_window_index - start_window_index + 1)
        char_tracker[string[end_window_index]] = end_window_index
    return longest_size


if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", "abc", 3),
        ("bbbbb", "b", 1),
        ("pwwkew", "wke", 3),
        ("", "", 0),
        ("a", "a", 1),
        ("abcdbc", "abcd", 4),
        ("aaaaab", "ab", 2),
        ("dvdf", "vdf", 3)
    ]

    for string, substring, expected_result in test_cases:
        result = longest_substring_version3(string)
        print(string, substring, result)
        assert result == expected_result

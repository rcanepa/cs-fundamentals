"""We say that two words are related if they differ by only a single swap of
distinct characters. For example, converse and conserve are related
(because you can swap the v and the s). Provide a function that determines
whether two input words are related.

Two words are n-related if they differ by exactly n disjoint pairs of swapped
characters. For example, "abcd" and "badc" are 2-related. However, "abcd" and
"bcda" are not 3-related. (You can get from "abcd" to "bcda" in 3 swaps, but
they are not disjoint.) Provide a function that determine whether two input
words are n-related for an additional input value n."""


from collections import defaultdict


def are_related(s1, s2, nrelated):
    if s1 is None or s2 is None:
        raise Exception("you must provide two strings")

    if len(s1) != len(s2):
        return False

    s1_letters = defaultdict(int)
    s2_letters = defaultdict(int)

    # TC O(N), where N = len(s1)
    for c in s1:
        s1_letters[c] += 1

    # TC O(N)
    for c in s2:
        s2_letters[c] += 1

    # TC O(M), where M = len(s2_letters.keys())
    if s1_letters != s2_letters:
        return False

    # TC O(N)
    d = {}
    swaps = 0
    for i in range(len(s1)):
        # print(d)
        if s1[i] != s2[i] and not (s2[i], s1[i]) in d:
            d[(s1[i], s2[i])] = True
        elif s1[i] != s2[i] and (s2[i], s1[i]) in d:
            print(d)
            swaps += 1
            d.pop((s2[i], s1[i]))
            # d.pop((s1[i], s2[i]))

    print("swaps = ", swaps)
    return swaps == nrelated


if __name__ == "__main__":
    s1 = "abbcd"
    s2 = "babdc"
    print(are_related(s1, s2, 2))

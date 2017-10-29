"""459. Repeated Substring Pattern
https://leetcode.com/problems/repeated-substring-pattern/description/

Given a non-empty string check if it can be constructed by taking a substring of
it and appending multiple copies of the substring together. You may assume the given
string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n):
            if n % (n - i) == 0:
                suffix = s[i:]
                if suffix * (n // len(suffix)) == s:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        ("abcabcabcabc", True),
        ("abab", True),
        ("abc", False),
        ("aaaabaaaab", True),
        ("aa", True),
        ("ab", False)
    ]

    for pattern, expect in test_cases:
        result = s.repeatedSubstringPattern(pattern)
        if result == expect:
            print("ok ->", result)
        else:
            print("nok ->", result)
            break

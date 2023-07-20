"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""
from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        aux = self._createAux(needle)
        print(aux)

        i = 0
        j = 0

        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                continue

            if j > 0:
                j = aux[j - 1]
                continue

            i += 1

        if j < len(needle):
            return -1
        return i - j

    def _createAux(self, pattern: str) -> List[int]:
        aux = [0] * len(pattern)

        m = 0
        i = 1

        while i < len(pattern):
            if pattern[m] == pattern[i]:
                m += 1
                aux[i] = m
                i += 1
                continue

            if pattern[m] != pattern[i] and m > 0:
                m = aux[m - 1]
                continue

            aux[i] = m
            i += 1

        return aux


if __name__ == "__main__":
    solution = Solution()

    print(solution.strStr("deadElephant", "abcabcabcabc"))

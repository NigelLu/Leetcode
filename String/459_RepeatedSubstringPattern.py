"""
Given a string s,
check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
 

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.
"""
from typing import List


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not len(s):
            return True

        nextArr = self._getNextArr(s)

        return nextArr[-1] and (len(s) % (len(s) - nextArr[-1]) == 0)

    def _getNextArr(self, s: str) -> List[int]:
        nextArr = [0] * len(s)

        i = 1
        m = 0
        while i < len(s):
            if s[i] == s[m]:
                m += 1
                nextArr[i] = m
                i += 1
                continue

            if m > 0:
                m = nextArr[m - 1]
                continue

            i += 1

        return nextArr


if __name__ == "__main__":
    solution = Solution()

    print(solution.repeatedSubstringPattern("abac"))

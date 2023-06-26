"""
Given a string s and an integer k, 
reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them.

If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and leave the other as original.

 
Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"


Example 2:
Input: s = "abcd", k = 2
Output: "bacd"
 

Constraints:
1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104
"""

from typing import List


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        idx = 0
        sList = list(s)

        while idx <= len(sList) - 2 * k:
            self._reverseSubStr(sList, idx, k)
            idx += 2 * k
        
        self._reverseSubStr(sList, idx, min(k, len(sList) - idx))

        return "".join(sList)

    def _reverseSubStr(self, s: List[str], start: int, length: int):
        for offset in range(0, length // 2):
            s[start + offset], s[start + length - offset - 1] = (
                s[start + length - offset - 1],
                s[start + offset],
            )

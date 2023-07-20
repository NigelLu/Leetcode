"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.

 
Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:
1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""

from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        sList = list(s)
        if len(sList) <= 0: return s

        start = 0
        end = len(sList) - 1

        # * remove leading spaces
        while start < end and sList[start] == " ":
            sList[start] = ""
            start += 1

        # * remove trailing spaces
        while end > start and sList[end] == " ":
            sList[end] = ""
            end -= 1

        slow_idx = start
        
        while slow_idx <= end:
            if sList[slow_idx] != " ":
                # * locate the end of the word
                fast_idx = slow_idx
                while fast_idx <= end and sList[fast_idx] != " ":
                    fast_idx += 1
                
                # * reverse the word
                self._reverseSubStr(sList, slow_idx, fast_idx - slow_idx)
            else:
                # * locate the start of the next word
                fast_idx = slow_idx + 1
                while sList[fast_idx] == " ":
                    sList[fast_idx] = ""
                    fast_idx += 1

            slow_idx = fast_idx

        self._reverseSubStr(sList, start, end - start + 1)
        return "".join(sList)
            
    def _reverseSubStr(self, sList: List[str], start: int, length: int) -> None:
        for offset in range(length // 2):
            sList[start + offset], sList[start + length - offset - 1] = (
                sList[start + length - offset - 1],
                sList[start + offset],
            )

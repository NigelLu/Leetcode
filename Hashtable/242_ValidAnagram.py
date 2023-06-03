"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true


Example 2:
Input: s = "rat", t = "car"
Output: false
 

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # * not anagram if length mismatches
        if len(s) != len(t): return False

        # * 26 lower-case English letters in total
        counter_s = [0] * 26
        counter_t = [0] * 26

        ord_a = ord("a")
        for idx in range(len(s)):
            counter_s[ord(s[idx]) - ord_a] += 1
            counter_t[ord(t[idx]) - ord_a] += 1

        for idx in range(26):
            if counter_t[idx] != counter_s[idx]: return False
        
        return True
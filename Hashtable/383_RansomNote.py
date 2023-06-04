"""
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # * logic is to first count the letters in magazine
        # * then check if they can construct ransom note
        ord_a = ord("a")
        magazine_counter = [0] * 26

        for char in magazine:
            magazine_counter[ord(char) - ord_a] += 1

        for char in ransomNote:
            magazine_counter[ord(char) - ord_a] -= 1

        for count in magazine_counter:
            if count < 0: return False

        return True

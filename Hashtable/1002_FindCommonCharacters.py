"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.


Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""

from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # * init result counter
        result_counter = [None] * 26
        ord_a = ord("a")

        for word in words:
            # * temporary word counter
            word_counter = [0] * 26

            # * iterate and count
            for letter in word:
                word_counter[ord(letter) - ord_a] += 1

            # * update result counter
            for idx, count in enumerate(word_counter):
                result_counter[idx] = (
                    count
                    if result_counter[idx] is None or result_counter[idx] > count
                    else result_counter[idx]
                )
        # * init result
        result = []

        # * fill result array
        for idx, count in enumerate(result_counter):
            current_char = chr(idx + ord_a)
            result.extend([current_char] * (count if count else 0))

        return result

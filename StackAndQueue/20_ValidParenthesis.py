"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false


Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
import queue


class Solution:
    def __init__(self):
        self.stack = queue.LifoQueue()
        self.leftParentheses = ["{", "[", "("]
        self.rightParentheses = ["}", "]", ")"]

    def isValid(self, s: str) -> bool:
        # * empty the stack if none empty
        while self.stack.not_empty:
            self.stack.get()

        for char in s:
            # * if is open brackets, then push to stack
            if char in self.leftParentheses:
                self.stack.put(char)
                continue

            # * if no open brackets in stack but encountered a closing bracket, then return False
            if self.stack.empty:
                return False

            # * top of the stack does not match char, then return False
            if self.stack.get() != char:
                return False

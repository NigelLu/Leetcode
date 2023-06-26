"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。


示例 1:

输入: s = "We are happy."
输出："We%20are%20happy."

限制：

0 <= s 的长度 <= 10000
"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        spaceCount = 0
        for char in s: spaceCount += (char == " ")

        sList = [None] * (len(s) + spaceCount * 2)

        fast_idx = len(sList) - 1
        for slow_idx in range(len(s) - 1, -1, -1):
            if s[slow_idx] != " ":
                sList[fast_idx] = s[slow_idx]
                fast_idx -= 1
                continue
            
            sList[fast_idx - 2], sList[fast_idx - 1], sList[fast_idx] = ("%", "2", "0")
            fast_idx -= 3
        
        return "".join(sList)
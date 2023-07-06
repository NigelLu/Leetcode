"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2, 该函数将返回左旋转两位得到的结果"cdefgab"。


示例 1:
输入: s = "abcdefg", k = 2
输出: "cdefgab"


示例 2:
输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
 

限制:
1 <= k < s.length <= 10000
"""
from typing import List


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s_list = list(s)
        s_list.extend([None for _ in range(n)])
        s_len = len(s_list)

        for offset in range(n):
            s_list[offset], s_list[s_len - n + offset] = "", s_list[offset]

        return "".join(s_list)


class AlternateSolution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s_list = list(s)
        s_len = len(s_list)

        self._reverseStr(s_list, 0, n)
        self._reverseStr(s_list, n, s_len)

        self._reverseStr(s_list, 0, s_len)

        return "".join(s_list)

    def _reverseStr(self, s: List[str], start: int, end: int) -> None:
        for offset in range(0, (end - start) // 2):
            s[start + offset], s[end - offset - 1] = (
                s[end - offset - 1],
                s[start + offset],
            )

        return


if __name__ == "__main__":
    alternateSolution = AlternateSolution()
    print(alternateSolution.reverseLeftWords("abcdefg", 2))

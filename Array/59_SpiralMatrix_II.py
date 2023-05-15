"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]


Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
"""


from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[None] * n for _ in range(n)]

        cur_ele = 1
        cur_position = [0, 0]
        cur_direction = [0, 1]
        row_limits = [0, n-1]  # * [lower, upper]
        col_limits = [0, n-1]  # * [lower, upper]

        while cur_ele <= n ** 2:
            result[cur_position[0]][cur_position[1]] = cur_ele
            cur_ele += 1

            next_position = [cur_position[0] + cur_direction[0],
                             cur_position[1] + cur_direction[1]]

            # * row out of bound
            if next_position[0] < row_limits[0]:
                cur_direction = [0, 1]
                col_limits[0] += 1

            elif next_position[0] > row_limits[1]:
                cur_direction = [0, -1]
                col_limits[1] -= 1

            # * col out of bound
            elif next_position[1] < col_limits[0]:
                cur_direction = [-1, 0]
                row_limits[1] -= 1

            elif next_position[1] > col_limits[1]:
                cur_direction = [1, 0]
                row_limits[0] += 1

            # * update the current position with adjusted current direction
            cur_position = [cur_position[0] + cur_direction[0],
                            cur_position[1] + cur_direction[1]]

        return result

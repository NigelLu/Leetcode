"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].


Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, 
could you find an O(n) solution using a different approach?
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [None] * len(nums)
        cur_idx = len(nums) - 1
        slow_idx, fast_idx = 0, len(nums) - 1

        while slow_idx <= fast_idx:
            slow_squared = nums[slow_idx] ** 2
            fast_squared = nums[fast_idx] ** 2

            if slow_squared < fast_squared:
                result[cur_idx] = fast_squared
                fast_idx -= 1
            else:
                result[cur_idx] = slow_squared
                slow_idx += 1

            cur_idx -= 1

        return result

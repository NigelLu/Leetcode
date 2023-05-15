"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.


Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1


Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which 
the time complexity is O(n log(n)).
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum_length = float("inf")

        cur_sum = 0
        start_idx, end_idx = 0, 0

        # * go through the Array
        while end_idx < len(nums):

            # * expand the subarray until it is no smaller than target, or the end_idx out of range
            while cur_sum < target:
                cur_sum += nums[end_idx]
                end_idx += 1

                if end_idx >= len(nums):
                    break

            # * squeeze the subarray until it is smaller than target, update the min_length along the way
            while cur_sum >= target:
                new_length = end_idx - start_idx
                minimum_length = minimum_length if minimum_length < new_length else new_length
                cur_sum -= nums[start_idx]
                start_idx += 1

        return minimum_length if minimum_length <= len(nums) else 0

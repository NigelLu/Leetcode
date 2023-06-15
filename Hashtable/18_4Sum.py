"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 
Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        len_nums = len(nums)

        if len_nums < 4 or (nums[0] > target and nums[0] > 0):
            return result

        first = 0
        # * there must be at least 3 elements after first
        while first <= len_nums - 4:
            fourth = len_nums - 1
            # * there must be at least 2 elements in between first and fourth
            while fourth >= first + 3:
                # * now the problem falls back to finding two elements that sum up to a certain target
                second, third = first + 1, fourth - 1
                while second <= third - 1:
                    cur_sum = nums[first] + nums[second] + nums[third] + nums[fourth]

                    if cur_sum > target:
                        third -= 1
                        continue

                    if cur_sum == target:
                        result.append(
                            [nums[first], nums[second], nums[third], nums[fourth]]
                        )

                        # * de-duplicate the third element (doesn't matter if we do that only on the second/third element)
                        # * here for best performance, I would do it on both
                        second_ele = nums[second]
                        while second_ele == nums[second] and second <= third - 1:
                            second += 1

                        third_ele = nums[third]
                        while third_ele == nums[third] and second <= third - 1:
                            third -= 1
                        continue

                    if cur_sum < target:
                        second += 1

                # * de-duplicate the fourth element
                fourth_ele = nums[fourth]
                while fourth_ele == nums[fourth] and fourth >= first + 3:
                    fourth -= 1

            # * de-duplicate the first element (!unnecessary, but I do it for performance)
            first_ele = nums[first]
            while first_ele == nums[first] and first <= len_nums - 4:
                first += 1

        return result

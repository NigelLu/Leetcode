"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, 
return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0


Example 2:
Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
 

Constraints:
n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
"""

from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map_i = {}
        sum_map_ii = {}
        nums_len = len(nums1)

        for idx_i in range(nums_len):
            for idx_ii in range(nums_len):
                sum_i, sum_ii = nums1[idx_i] + \
                    nums2[idx_ii],  nums3[idx_i] + nums4[idx_ii]

                if sum_i in sum_map_i:
                    sum_map_i[sum_i] += 1
                else:
                    sum_map_i[sum_i] = 1

                if sum_ii in sum_map_ii:
                    sum_map_ii[sum_ii] += 1
                else:
                    sum_map_ii[sum_ii] = 1

        count = 0
        for sum_i in sum_map_i:
            if -sum_i in sum_map_ii:
                count += sum_map_i[sum_i] * sum_map_ii[-sum_i]

        return count

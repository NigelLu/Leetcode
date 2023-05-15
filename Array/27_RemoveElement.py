"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, 
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.


Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).


Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

from typing import List

# ! non-optimal
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur_idx = 0
        swap_idx = len(nums) - 1

        while cur_idx < swap_idx:
            if nums[cur_idx] == val:
                nums[cur_idx], nums[swap_idx] = nums[swap_idx], nums[cur_idx]
                swap_idx -= 1
                continue
            cur_idx += 1
        
        if cur_idx < len(nums) and nums[cur_idx] == val: return cur_idx

        return cur_idx + 1


# * optimal solution

# * NOTE: should use slow-fast index
# * where slow tracks how many elements satisfy the condition and fast tracks the index for iteration
class OptimalSolution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow_idx = fast_idx = 0

        while fast_idx < len(nums):
            if nums[fast_idx] != val: 
                nums[slow_idx] = nums[fast_idx]
                slow_idx += 1
            fast_idx += 1

        return slow_idx
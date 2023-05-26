"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
 

Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
      # * init the tracker
      A, B = headA, headB
      
      # * go through both linked lists
      # * track the difference in lengths
      while A and B:
          A, B = A.next, B.next

      # * init two new trackers
      cur_A, cur_B = headA, headB

      # * forward the trackers
      # * number of steps is the difference in length
      while A:
          cur_A, A = cur_A.next, A.next
      while B:
          cur_B, B = cur_B.next, B.next

      # * now that the length are aligned
      # * iterate through both linked lists
      while cur_A and cur_B:
          if id(cur_A) == id(cur_B): return cur_A
          cur_A, cur_B = cur_A.next, cur_B.next

      # * no intersection found, return None
      return None
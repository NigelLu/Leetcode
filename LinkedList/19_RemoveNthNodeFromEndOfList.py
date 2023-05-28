"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]


Example 2:
Input: head = [1], n = 1
Output: []


Example 3:
Input: head = [1,2], n = 1
Output: [1]
 

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        sentinel = ListNode(val=None, next=head)
        slow_prev = sentinel
        slow = head
        # * init fast
        fast = head
        counter = n
        while fast and counter - 1:
            fast = fast.next
            counter -= 1

        if counter - 1:
            return head

        # * move forward till end
        while fast.next:
            slow_prev, slow = slow, slow.next
            fast = fast.next

        # * remove the nth node
        slow_prev.next = slow.next

        return sentinel.next

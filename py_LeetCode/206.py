# Reverse Linked List
# Runtime: 44 ms, faster than 77.06% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.3 MB, less than 93.71% of Python3 online submissions for Reverse Linked List.
# https://leetcode.com/submissions/detail/734272423/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current
        return prev

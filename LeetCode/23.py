from typing import List, Optional
import heapq
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None:
            return lists
        temp = ListNode(-1)
        tail = temp
        for i in range(len(lists)):
            pointer = lists[i]
            while pointer:
                tail.next = pointer
                tail = tail.next
                pointer = pointer.next
        return self.solve(temp.next)

    def solve(self, node):
        values = []
        head = node
        while node:
            values.append(node.val)
            node = node.next
        values = collections.deque(sorted(values))
        node = head
        while node:
            node.val = values.popleft()
            node = node.next
        return head

# Runtime: 79 ms, faster than 99.95% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 17.6 MB, less than 94.70% of Python3 online submissions for Merge k Sorted Lists.

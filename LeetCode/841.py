# Keys and Rooms
# Runtime: 73 ms, faster than 84.19% of Python3 online submissions for Keys and Rooms.
# Memory Usage: 14.5 MB, less than 52.60% of Python3 online submissions for Keys and Rooms.
# https://leetcode.com/submissions/detail/726756666/

from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        hash_set = set()
        queue = deque([0])
        while queue:
            current = queue.popleft()
            if current in hash_set:
                continue
            hash_set.add(current)
            for i in rooms[current]:
                queue.append(i)
        return len(hash_set) == len(rooms)


print(Solution().canVisitAllRooms([[1], [2], [3], []]))

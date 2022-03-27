from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength = sorted((sum(row), idx)  for idx, row in enumerate(mat))[:k]
        return [i[1] for i in strength]



print(Solution.kWeakestRows("", [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3))
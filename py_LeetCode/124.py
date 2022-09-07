# Binary Tree Maximum Path Sum
# Runtime: 87 ms, faster than 95.29% of Python3 online submissions for Binary Tree Maximum Path Sum.
# Memory Usage: 21.3 MB, less than 93.77% of Python3 online submissions for Binary Tree Maximum Path Sum.
# https://leetcode.com/submissions/detail/731604995/

from typing import List, Optional

from drawtree import draw_level_order


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """strat: preorder DFS + recursion"""
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            # returns sum of respective side of tree. does not include child if child is negative.
            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)
            # update result if sum of new subtree (inclusive of splits) is larger than result.
            res[0] = max(res[0], root.val + left_max + right_max)
            # return sum of subtree (WITHOUT SPLIT).
            return root.val + max(left_max, right_max)

        dfs(root)
        return res[0]


def to_binary_tree(items: List):
    it = iter(items)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root


draw_level_order("[-10, 9, 20, 0, 0, 15, 7]")
print(Solution().maxPathSum(to_binary_tree([-10, 9, 20, None, None, 15, 7])))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, root.val)]

        while len(stack) > 0:
            cur, cur_sum = stack.pop()

            if not cur.left and not cur.right:
                if cur_sum == targetSum:
                    return True

            if cur.left:
                stack.append((cur.left, cur_sum + cur.left.val))

            if cur.right:
                stack.append((cur.right, cur_sum + cur.right.val))

        return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        min = sys.maxsize

        if not root:
            return 0

        while len(stack) > 0:
            cur, dist = stack.pop()

            if not cur.left and not cur.right:
                if dist < min:
                    min = dist

            if cur.left:
                stack.append((cur.left, dist + 1))

            if cur.right:
                stack.append((cur.right, dist + 1))

        return min

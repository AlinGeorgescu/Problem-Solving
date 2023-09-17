# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        minHeight = sys.maxsize
        maxHeight = 0

        if not root:
            return True

        stack = [(root, 1)]

        while len(stack) > 0:
            cur, length = stack.pop()

            if not cur.left or not cur.right:
                if minHeight > length:
                    minHeight = length

                if maxHeight < length:
                    maxHeight = length

            if cur.left:
                stack.append((cur.left, length + 1))

            if cur.right:
                stack.append((cur.right, length + 1))

        return maxHeight <= minHeight + 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [root.left, root.right]
        index = 0

        while index < len(queue):
            first = queue[index]
            second = queue[index + 1]
            index += 2

            if first is None and second is None:
                continue
            elif first is None or second is None or first.val != second.val:
                return False
            else:
                queue.append(first.left)
                queue.append(second.right)
                queue.append(first.right)
                queue.append(second.left)

        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [p, q]
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
                queue.append(second.left)
                queue.append(first.right)
                queue.append(second.right)

        return True
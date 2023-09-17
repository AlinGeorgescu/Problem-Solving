# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)

        if length == 0:
            return None

        mid = length // 2

        left = self.sortedArrayToBST(nums[ : mid])
        right = self.sortedArrayToBST(nums[mid + 1 : ])
        return TreeNode(nums[mid], left, right)

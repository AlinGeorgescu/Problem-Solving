#!/usr/bin/env python3

from typing import List

class Solution:
    def dfs(self, node : TreeNode, isLonely : bool) -> None:
        if not node:
            return
        if isLonely:
            self.res.append(node.val)

        dfs(node.left, node.right == None)
        dfs(node.right, node.left == None)

    def getLonelyNodes(self, root : TreeNode) -> List[int]:
        self.res = []

        dfs(root, False)

        return self.res

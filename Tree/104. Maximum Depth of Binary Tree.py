# dfs
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lefth = self.maxDepth(root.left)
        righth = self.maxDepth(root.right)

        return max(lefth,righth)+1
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [float("-inf")]
        def dfs(node):
            if not node:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            left_max = max(0,left_max)
            right_max = max(0,right_max)
            ans[0] = max(ans[0], node.val+left_max+right_max)
            return node.val+max(left_max,right_max)
        dfs(root)
        return ans[0]
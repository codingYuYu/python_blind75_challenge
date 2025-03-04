class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        # 左右子樹互換
        temp = root.left
        root.left = root.right
        root.right = temp

        # invert節點
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
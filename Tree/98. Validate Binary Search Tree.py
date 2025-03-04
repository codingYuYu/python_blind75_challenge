class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if node:
                if not inorder(node.left):
                    return False
                if node.val <= self.prev:
                    return False
                self.prev = node.val
                if not inorder(node.right):
                    return False
            return True
        self.prev = -math.inf
        return inorder(root)
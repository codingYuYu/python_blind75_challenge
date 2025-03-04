class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.is_same(root, subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

    def is_same(self,p,q):
        if not p and not q:
           return True
        if not p and q:
            return False
        if p and not q:
            return False
        if p.val != q.val:
            return False
        return (self.is_same(p.left, q.left) and self.is_same(p.right,q.right))
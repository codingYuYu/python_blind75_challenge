class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder(root,ans=None):
            if ans is None:
                ans = []
            if root:
                ans.append(root.val)
                preorder(root.left,ans)
                preorder(root.right,ans)
            # 如果該子樹沒有節點，則用None填充
            else:
                ans.append(None)
            return ans
        return preorder(p)==preorder(q)
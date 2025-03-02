from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return copy.deepcopy(node)


# DFS
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        seen = {}
        def dfs(node):
            # Step 1: Make out node
            copy = Node(node.val)
            seen[copy.val] = copy            
            # Step 2: Add neighbors
            for i in node.neighbors:
                if i.val in seen:
                    copy.neighbors.append(seen[i.val])
                else:
                    copy.neighbors.append(dfs(i))
            return copy

        return dfs(node)
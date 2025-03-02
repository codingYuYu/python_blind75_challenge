class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i:[] for i in range(numCourses)}
        for i in prerequisites:
            pre_map[i[0]].append(i[1])

        visited = set()
        # 檢查是否先修課程之間形成環
        def dfs(crs):
            if crs in visited:
                return False
            if pre_map[crs]==[]:
                return True
            
            visited.add(crs)
            for pre in pre_map[crs]:
                if dfs(pre)==False:
                    return False
                else:
                    pre_map[crs].remove(pre)
            visited.remove(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c)==False:
                return False
        return True
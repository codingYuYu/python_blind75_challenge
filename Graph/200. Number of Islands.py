class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        count = 0

        visited = set()
        def dfs(visited,row,col):
            if row<0 or row>=rows or col<0 or col>=cols:
                return
            if grid[row][col]=="0":
                return 
            if (row,col) in visited:
                return 
            visited.add((row,col))

            dfs(visited, row+1, col) 
            dfs(visited, row-1, col) 
            dfs(visited, row, col+1) 
            dfs(visited, row, col-1) 
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j]!="0":
                    dfs(visited,i,j)
                    count+=1
        return count
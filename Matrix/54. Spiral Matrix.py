class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        visited = set()
        ans = []
        x = 0
        y = 0
        mx = 0
        my = 1
        for i in range(row * col):
            ans.append(matrix[x][y])
            visited.add((x,y))

            if not (0 <= y + my < col) or not (0 <= x + mx < row) or (x + mx, y + my) in visited:
                mx, my = my, -mx

            x += mx
            y += my

        return ans
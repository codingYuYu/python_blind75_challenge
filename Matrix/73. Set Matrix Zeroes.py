# fast
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        zerothRow = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r == 0:
                        zerothRow = True

                    else:
                        matrix[r][0] = 0


        for r in range (1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0:
                    matrix[r][c] = 0

                if matrix[r][0] == 0:
                    matrix[r][c] = 0


        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        if zerothRow:
            for c in range(COLS):
                matrix[0][c] = 0

# slow
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])

        visited = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0 and (i,j) not in visited:
                    for a in range(row):
                        if matrix[a][j] != 0:
                            matrix[a][j] = 0
                            visited.add((a,j))
                    for b in range(col):
                        if matrix[i][b] != 0:
                            matrix[i][b] = 0
                            visited.add((i,b))

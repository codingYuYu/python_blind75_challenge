class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        def check(row,col,l):
            if l == len(word):
                return True
            if not 0<=row<rows or not 0<=col<cols or (row,col) in visited or board[row][col] != word[l]:
                return False
            visited.add((row,col))
            res = check(row+1,col,l+1) or check(row-1,col,l+1) or check(row,col+1,l+1) or check(row,col-1,l+1)
            visited.remove((row,col))
            return res

        count = {}
        for c in word:
            count[c] = 1+count.get(c,0)

        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        for r in range(rows):
            for c in range(cols):
                if check(r, c, 0): return True
        return False
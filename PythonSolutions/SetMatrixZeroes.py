class Solution: 
    def setZeroes(self, matrix: list[list[int]]) -> None:
        N, M = len(matrix[0]), len(matrix)
        first_row, first_col = False, False
        for r in range(M):
            if matrix[r][0] == 0: first_col = True
        for c in range(N):
            if matrix[0][c] == 0: first_row = True

        for r in range(1,M):
            for c in range(1,N):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1,M):
            if matrix[r][0] == 0:
                for c in range(1,N):
                    matrix[r][c] = 0
        
        for c in range(1,N):
            if matrix[0][c] == 0:
                for r in range(1,M):
                    matrix[r][c] = 0

        if first_row:
            for c in range(N): matrix[0][c] = 0
        if first_col: 
            for r in range(M): matrix[r][0] = 0
        
        return matrix

solution = Solution()
print(solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
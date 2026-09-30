class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = []

        def dfs(r, c, lands):

            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == 0:
                return 

            lands.add((r, c))
            visited.add((r,c))
            
            dfs(r + 1, c, lands)
            dfs(r - 1, c, lands)
            dfs(r, c + 1, lands)
            dfs(r, c - 1, lands)

            islands.append(len(lands ))

            

            


        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    dfs(row, col, set())
       
        if len(islands) == 0:
            return 0
        return max(islands)
        
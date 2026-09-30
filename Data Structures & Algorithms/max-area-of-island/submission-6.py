class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c, lands):

            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == 0:
                return 0

            
            visited.add((r,c))
            
            
            return 1 + dfs(r + 1, c, lands) + dfs(r - 1, c, lands) +dfs(r, c + 1, lands) + dfs(r, c - 1, lands)


        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = dfs(row, col, 0)
                    if area > islands:
                        islands = area
                     
       
        # if len(islands) == 0:
        #     return 0
        return islands
        
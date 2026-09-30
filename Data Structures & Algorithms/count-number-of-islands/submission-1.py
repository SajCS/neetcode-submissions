class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # islands = []
        counter = 0

        def dfs(r, c, visit):
            
            ROWS, COLS = len(grid), len(grid[0])

            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == "0":
                return False

            # visit.add((r,c))
            grid[r][c] = "0"


            dfs(r+1,c, visit)
            dfs(r-1, c, visit)
            dfs(r, c +1, visit)
            dfs(r, c-1, visit)

            # visit.pop()
            

            # islands.append(visit.copy())

            return True
        

        for row in range(len(grid)):
        
            for col in range(len(grid[row])):
                if dfs(row, col, set()):
                    counter+= 1
       
        return counter


            

        
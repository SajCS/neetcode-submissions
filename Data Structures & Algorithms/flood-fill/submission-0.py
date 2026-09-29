class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oColor = image[sr].copy()[sc]

        def dfs(r, c, visit):
            ROWS, COLS = len(image), len(image[0])

            if min(r,c) < 0 or r == ROWS or c == COLS or (r, c) in visit or image[r][c] != oColor:
                return 
            
            image[r][c] = color
            visit.add((r, c))
            


            

            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c -1, visit)
            

        
            
           
        dfs(sr, sc, set())
        return image
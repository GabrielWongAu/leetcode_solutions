# https://leetcode.com/problems/number-of-islands/

from collections import deque

class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited=set()
        islands=0

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
        
            while q:
                row, col = q.popleft()
                directions= [[1,0],[-1,0],[0,1],[0,-1]]
              
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r ,c) not in visited):
                        q.append((r , c ))
                        visited.add((r, c ))

        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands +=1 

        return islands

# Time complexity: O(m * n) 
# Where m is the number of rows and n is the number of columns.

# Space complexity: O(min(m,n))
# Because in worst case where the grid is filled with lands, 
# the size of queue can grow up to min(m, n).
"""
# ✅ 1. **Most Common Solution** — **BFS** (Level-order Traversal)

### 🧠 Intuition:

- This is a classic **shortest path on unweighted grid** → use **Breadth-First Search (BFS)**.
- Each cell is a node; 8-directional movement = graph edges.
- Start from `(0, 0)` and expand level-by-level, marking visited nodes
- Have a visited array to mark each cell as True (visited)
- create a directions array to check for each direction
- if condition is important

"""

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        
        queue = [(0, 0, 1)]  # (row, col, path_length)
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while queue:
            r, c, dist = queue.pop(0)
            if r == n - 1 and c == n - 1:
                return dist
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))
        
        return -1

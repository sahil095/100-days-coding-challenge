class Solution:
    def deleteGreatestValue(self, grid):
        for row in grid:
            row.sort()  # sort each row once

        answer = 0
        n = len(grid[0])

        for col in range(n - 1, -1, -1):  # start from last column
            max_val = 0
            for row in grid:
                max_val = max(max_val, row[col])
            answer += max_val

        return answer

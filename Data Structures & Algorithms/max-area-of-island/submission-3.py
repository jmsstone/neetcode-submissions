class Solution:
    def valid(self,x,y,grid):
        return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[x])
    def dfs(self, x, y, grid, count):
        if not self.valid(x,y,grid):
            return 0
        grid[x][y] = 0
        count += 1
        for i in range(x-1,x+2):
            if x==i:
                continue
            if self.valid(i,y, grid) and grid[i][y] == 1:
                count = self.dfs(i,y,grid,count)
        for j in range(y-1,y+2):
            if y==j:
                continue
            if self.valid(x,j, grid) and grid[x][j] == 1:
                count = self.dfs(x,j,grid,count)
        return count
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        counts = [0]
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                count = 0
                if grid[x][y] == 1:
                    count = self.dfs(x,y,grid, count)
                    counts.append(count)
        return max(counts)
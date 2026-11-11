class Solution:
    def valid(self,x,y,grid):
        return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[x])
    def dfs(self,x,y,grid):
        if not self.valid(x,y,grid):
            return
        grid[x][y] = 0
        for i in range(x-1, x+2):
            if i == x:
                continue
            if self.valid(i,y,grid) and grid[i][y] == "1":
                self.dfs(i,y,grid)
        for j in range(y-1, y+2):
            if j == y:
                continue
            if self.valid(x,j,grid) and grid[x][j] == "1":
                self.dfs(x,j,grid)
        return
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    self.dfs(x,y,grid)
                    count += 1
        return count


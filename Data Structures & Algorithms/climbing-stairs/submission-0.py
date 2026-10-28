class Solution:
    def climbStairsHelper(self, n, visited):
        if n in visited:
            return visited[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        else:
            visited[n] = self.climbStairsHelper(n-1,visited) + self.climbStairsHelper(n-2,visited)
            return visited[n]
            
    def climbStairs(self, n: int) -> int:
        visited = {}
        return self.climbStairsHelper(n,visited)
        
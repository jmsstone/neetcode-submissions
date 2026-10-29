class Solution:
    def climbStairsHelper(self, n, cost, visited):
        if n == 0:
            return cost[n]
        if n == 1:
            return cost[n]
        if n in visited:
            return visited[n]
        else:
            visited[n] = cost[n] + min(self.climbStairsHelper(n-1,cost,visited), self.climbStairsHelper(n-2,cost,visited)) 
            return visited[n]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        visited = {}
        n = len(cost)
        return min(
            self.climbStairsHelper(n-1, cost, visited), 
            self.climbStairsHelper(n-2, cost, visited)
        )
        
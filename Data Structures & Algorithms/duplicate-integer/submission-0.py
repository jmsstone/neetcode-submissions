class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = []
        for n in nums:
            if n not in visited:
                visited.append(n)
            else:
                return True
        return False
        
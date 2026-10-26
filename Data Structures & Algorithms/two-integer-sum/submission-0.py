class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for n in range(len(nums)):
            if nums[n] not in visited:
                visited[target-nums[n]] = n
            else:
                return [visited[nums[n]],n]

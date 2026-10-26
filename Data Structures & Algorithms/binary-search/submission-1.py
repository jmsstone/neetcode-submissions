class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        mid = (left + right) // 2
        found = False
        while not found:
            print(nums[mid])
            if left > right:
                return -1
            if nums[mid] == target:
                return mid
            if (target > nums[mid]):
                left = mid+1
                mid = (left + right) // 2
                continue
            if (target < nums[mid]):
                right = mid-1
                mid = (left + right) // 2
                continue
            return -1
class Solution:
    def area(self, heights, left, right):
        width = right - left
        height = min(heights[left],heights[right])
        return width * height
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        areas = []
        while left < right:
            areas.append(self.area(heights,left,right))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max(areas)

        
        
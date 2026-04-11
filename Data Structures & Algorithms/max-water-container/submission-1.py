class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        max_area = 0
        while left < right:
            smallest_bar = min(heights[left], heights[right])
            curr_area = smallest_bar * (right - left)
            max_area = max(curr_area, max_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        max_area = 0
        for i in range(n):
            for j in range(n - 1, -1, -1):
                smallest_bar = min(heights[i], heights[j])
                curr_area = smallest_bar * (j - i)
                max_area = max(curr_area, max_area)

        return max_area


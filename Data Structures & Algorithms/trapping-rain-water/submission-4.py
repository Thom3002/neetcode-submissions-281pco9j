class Solution:

    # find max on right 
    # find max on left
    # calculate the area of water between:
    #   get the min between both maxes 
    # for every block in between subtract min_height - block_height and sum the result
    # 

    def trap(self, height: List[int]) -> int:
        left = 0
        n = len(height)
        right = n - 1
        left_max = right_max = 0
        water_area = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_area += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else: 
                    water_area += right_max - height[right]
                right -= 1
        return water_area
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[left]
        while left <= right:
            if nums[left] < nums[right]: # esta completamente ordenado
                res = min(res, nums[left])
                break
            
            mid = (right + left) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return res
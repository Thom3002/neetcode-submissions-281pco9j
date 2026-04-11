class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i, j in enumerate(nums):
            for k in range(i+1, n):
                if j == nums[k]:
                    return True
        
        return False

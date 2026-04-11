class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                min_idx = min(i, seen[diff])
                max_idx = max(i, seen[diff])
                return [min_idx, max_idx]
            seen[num] = i 

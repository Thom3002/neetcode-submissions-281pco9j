class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = set()

        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                    c = nums[right]
                elif s < 0:
                    left += 1

                else:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        
        return [list(t) for t in res]
        
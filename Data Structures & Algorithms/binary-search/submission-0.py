class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. get the middle number
        # 2. check if its bigger then the target
        # 3. if it is, set the right = mid
        # 4. repeat the process until t
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1


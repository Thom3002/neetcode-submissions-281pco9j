class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        output = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a = nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                b = nums[left]
                c = nums[right]
                s = a + b + c

                if s == 0:
                    output.append([a, b, c])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return output
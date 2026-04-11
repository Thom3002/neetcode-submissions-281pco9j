class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        while left != right:
            left_num = numbers[left]
            right_num = numbers[right]
            if left_num + right_num == target:
                return [left + 1, right + 1]
            elif left_num + right_num > target:
                right -= 1
            else:
                left += 1
        
        return [left + 1, right + 1]
            

        

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_sequence = 0
        for num in nums:
            if num - 1 not in nums:
                current = num
                sequence = 1
                while current + 1 in nums:
                    sequence += 1
                    current += 1

                
                max_sequence = max(sequence, max_sequence)
        return max_sequence


            
            

        
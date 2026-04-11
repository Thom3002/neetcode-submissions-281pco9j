class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            
        num_count = 0
        max_freq = 0
        output = []
        max_num = float("-inf")
        while num_count < k:
            for num, freq in count.items():
                if freq > max_freq and num not in output:
                    max_num, max_freq = num, freq
                else:
                    continue
            if max_num != float("-inf"):
                output.append(max_num)
            num_count += 1
            max_num = float("-inf")
            max_freq = 0
        return output

         

                


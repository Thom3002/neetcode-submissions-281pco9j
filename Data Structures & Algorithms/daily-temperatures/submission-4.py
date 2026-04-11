class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = n * [0]
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                popped_temp, popped_idx = stack.pop()
                res[popped_idx] = i - popped_idx
            
            stack.append((temp, i))
        return res

        # i, temp = 3, 36 
        # 36 > 30:
        # while temp > stack[-1][0]
            # 
        # stack = [(38, 1), (30, 2),  ]
        #   popped_temp, popped_idx = stack.pop()
        # 
        #   res[popped_idx] = i - popped_idx 
        # 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        count = 0
        stack_ind = 0
        stack = []
        stack.append((temperatures[0], 0))
        for i, t in enumerate(temperatures):
            while stack and temperatures[i] > stack[-1][0]:
                temp, popped_idx = stack.pop()
                result[popped_idx] = i - popped_idx
            if ((temperatures[i], i)) not in stack:
                stack.append((temperatures[i], i))
            # 30, 38, 30, 36, 35, 40 ,28
            # stack = [(30, 0)]
            # res = [0,0,0,0,0,0,0]

            # i = 0 
            # true temp[i] = 30 > 30 (false)
            # i = 1
            # true, 38 > 30:
                # 30, 0
                # res[0] = 1 - 0 = 1
            # i = 2 
        return result


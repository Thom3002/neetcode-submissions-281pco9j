class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            count = 0
            found_warmer_temp = False
            for j in range(i + 1, len(temperatures)):
                count += 1
                if temperatures[j] > temperatures[i]:
                    result.append(count)
                    found_warmer_temp = True
                    break
            if not found_warmer_temp:
                result.append(0)
            

        return result


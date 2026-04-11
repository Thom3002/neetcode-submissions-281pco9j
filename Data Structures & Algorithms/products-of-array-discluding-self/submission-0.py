class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)
        
        
        for i in range(n):
            product_aux = 1
            for j in range(n):
                if i == j:
                    continue
                else:
                    product_aux *= nums[j]
            output.append(product_aux)
            product_aux = 1
    
        return output
                


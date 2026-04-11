class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # n = len(nums)
        
        
        # for i in range(n):
        #     product_aux = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         else:
        #             product_aux *= nums[j]
        #     output.append(product_aux)
        #     product_aux = 1
    
        # return output

        # Now O(n)
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        sufix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= sufix
            sufix *= nums[i]
        
        return output



                


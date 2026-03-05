# 1. Calculate prefix products by multiplying all elements to the left.
# 2. Calculate suffix products by multiplying all elements to the right.
# 3. Multiply prefix and suffix values together to get the final result.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
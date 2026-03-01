# Two Sum - My Solution for the problem 

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                
                if nums[i] + nums[j] == target:
                    return [i, j]

# testing on local pc
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9)) 
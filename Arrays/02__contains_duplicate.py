# Problem 217: Contains Duplicate
# Approach: Sort the array to put duplicates next to each other, then check neighbors.
# Time Complexity: O(N log N) | Space Complexity: O(1)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
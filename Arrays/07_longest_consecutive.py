# 1. Convert the list to a set to remove duplicates and allow O(1) lookups.
# 2. Iterate through the set to ensure each unique number is processed only once.
# 3. Only count sequences starting from the smallest number (where n-1 is missing).

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        
        return longest
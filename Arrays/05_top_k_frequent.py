# 1. Count how many times each number appears using a dictionary.
# 2. Sort the numbers by their frequency in descending order.
# 3. Return the first 'k' most frequent numbers.

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        
        result = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        
        return result[:k]
# Problem 242: Valid Anagram
# Approach: Sort both strings. If they are anagrams, the sorted versions will match.
# Time Complexity: O(N log N) | Space Complexity: O(N)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
            
       
        return sorted(s) == sorted(t)
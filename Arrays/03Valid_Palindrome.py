# Day 3: Valid Palindrome (LeetCode #125)
# Approach: Data filtering and string reversal
# Complexity: Time O(n), Space O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for char in s:
            if char.isalnum():
                res.append(char.lower())
        
        clean_s = "".join(res)
        return clean_s == clean_s[::-1]
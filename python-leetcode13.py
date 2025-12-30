print("Leetcode 13: Valid Anagram")

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # I should have added the length check
        if len(s) != len(t):
            return False
        
        # compare sorted string 
        return sorted(s) == sorted(t)
        

# test cases 
sol = Solution()
s = "anagram"
t = "nagaram"
result = sol.isAnagram(s,t)
print(result) # should return true

print("Leetcode 8: First Unique Character in a String")

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # my solution to iterate through the string wasn't good, so I looked up a better solution see below:

        # create a dictionary to store character and its count
        char_count = {}

        for char in s:
            # if character is already in dictionary, increment its count
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # iterate through the string and find the index of first unique character
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index    
        return -1
        
# test cases
sol = Solution()
result = sol.firstUniqChar("leetcode")
print(result) # should return 0

sol2 = Solution()
result2 = sol2.firstUniqChar("loveleetcode")
print(result2) # should return 2

sol3 = Solution()
result3 = sol3.firstUniqChar("aabb")
print(result3) # should return -1
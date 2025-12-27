print("Leetcode 12: Contains Duplicate")

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # compare the length of the list with all the items and the distinctive items
        # if there is a gap, it means that the list includes at least one repeated item 
        return len(list(set(nums))) != len(nums)

# test cases 
sol = Solution()
nums = [1,2,3,1]
result = sol.containsDuplicate(nums)
print(result) # should return true


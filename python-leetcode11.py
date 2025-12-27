print("Leetcode 11: Number of Good Pairs")

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0

        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if(nums[i] == nums[j]):
                    result += 1

        
        return result

# test cases 
sol = Solution()
nums = [1,2,3,1,1,3]
result = sol.numIdenticalPairs(nums)
print(result) # should return 4


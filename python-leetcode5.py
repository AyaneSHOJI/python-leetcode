print("Leetcode 5: Two Sum")

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        n = len(nums)
        # loop through each pair of numbers in the list
        # first number is at index i, second number is at index j
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
                    # can be simplified
                    # return [i, j]
                    return answer
                
# test cases
sol = Solution()
result = sol.twoSum([3,2,3], 6)
print(result) # should return [0,2]

sol2 = Solution()
result2 = sol2.twoSum([3,2,4], 6)
print(result2) # should return [1,2]
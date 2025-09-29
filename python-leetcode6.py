print("Leetcode 6: Intersection of Two Arrays")

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # create distinct sets from both lists
        distinct_num1 = set(nums1)
        distinct_num2 = set(nums2)
        result = []

        # check if each number in distinct_num1 is in distinct_num2
        for num in distinct_num1:
            if num in distinct_num2:
                result.append(num)
        
        return result

        # optimized version from Copilot
        # Use set intersection operator for a concise solution
        # return list(set(nums1) & set(nums2))

# test cases
sol = Solution()
result = sol.intersection([4,9,5], [9,4,9,8,4])
print(result) # should return [9,4]

sol2 = Solution()
result2 = sol2.intersection([1,2,2,1], [2,2])
print(result2) # should return [2]
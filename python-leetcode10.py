print("Leetcode 10: ")

class Solution(object):
    def searchInsert(self, nums, target):

        # Here is my answer
        # The idea for getting the middle number is correct, but this function can not return the correct result in case of nums=[1] and target = 0


        # if target in nums :
        #     return nums.index(target)
        # else :
        #     middldIndex = (len(nums) -1)%2
        #     middleNum = nums[middldIndex]
        #     if(middleNum < target):
        #         for index in range(middldIndex, len(nums) -1) :
        #             if(nums[index] > target):
        #                 return index
        #             else:
        #                 return len(nums)
        #     else :
        #         for index in reversed(range(middldIndex,0)) :
        #             if(nums[index] < target):
        #                 return index + 1
        #             else:
        #                 return 0

        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # If not found, left will be at the correct insert position
        return left

# test cases 
sol = Solution()
nums = [1]
target = 0
result = sol.searchInsert(nums, target)
print(result) # should return 2


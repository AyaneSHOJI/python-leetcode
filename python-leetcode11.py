print("Leetcode 11: ")

class Solution(object):
    def moveZeroes(self, nums):
        
        # this is my solution, enumerate jumps always index that does not work
        # moreover, this solution has O(n²) time complexity + extra space (temp) – O(n) space.
        #
        # for index, number in enumerate(nums):
        #     if(number == 0):
        #         nums.pop(index)
        #         nums.append(0)

        # non zero pointer
        non_zero_index = 0
        
        # iterate through all elements
        for i in range(len(nums)):
            if nums[i] != 0:
                # switch if necessary
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1
        
        return nums

# test cases 
sol = Solution()
nums = [0,0,1]
result = sol.moveZeroes(nums)
print(result) # should return [1,0,0]


print("Leetcode 4: Kth Largest Element in a Stream")

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        # add the new value to the list
        self.nums.append(val)

        # sort the list in ascending order using bubble sort
        n = len(self.nums)
        for i in range(n):
            for j in range(0, n-i-1):
                # to understand how bubble sort evolve, uncomment the line below to see the process
                # print(self.nums)
                if self.nums[j] > self.nums[j+1]:
                    self.nums[j], self.nums[j+1] = self.nums[j+1], self.nums[j]
                    # equivalent code in C#:
                    # int temp = nums[j];
                    # nums[j] = nums[j + 1];
                    # nums[j + 1] = temp;
        # my error : self.k - 1 is the kth "smallest", read carefully the question...            
        return self.nums[n-self.k]
    
# test cases
kthLargest = KthLargest(3, [4,5,8,2])
print(kthLargest.add(3))   # return 4

# finally failed in LeetCode because of time limit exceeded
# I will try to use heap in the next 

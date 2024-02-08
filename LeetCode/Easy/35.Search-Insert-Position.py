class Solution(object):
    def searchInsert(self, nums, target):
        counter = 0
        for i in nums:
            if (i == target):
                return counter 
            elif (i > target):
                return counter 
            counter += 1
        return len(nums)

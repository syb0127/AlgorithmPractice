class Solution(object):
    def search(self, nums, target):
        if (target not in nums):
            return -1
        counter = 0
        for i in nums:
            if (i == target):
                return counter
            counter += 1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
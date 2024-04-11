class Solution(object):
    def containsDuplicate(self, nums):
        sofar = []
        if len(nums) == 1:
            return False
        for num in nums:
            if num in sofar:
                return True
            else:
                sofar.append(num)
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        
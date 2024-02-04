class Solution(object):
    def removeDuplicates(self, nums):
        numslength = 0
        seen = []
        copy = []
        for j in range(0, len(nums)):
            copy.append(nums[j])
        for i in range(0, len(copy)):
            if copy[i] not in seen:
                numslength += 1
                seen.append(copy[i])
            else:
                nums.remove(copy[i])
        return numslength
        """
        :type nums: List[int]
        :rtype: int
        """
        
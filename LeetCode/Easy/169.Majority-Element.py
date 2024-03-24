class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Boyer-Moore Voting Algorithm으로 공부할것 
        majority_sofar = None
        count = 0
        
        for i in range(len(nums)):
            if count == 0:
                majority_sofar = nums[i]
                print(majority_sofar)
            if (nums[i] == majority_sofar):
                count += 1
            else:
                count -=1
        return majority_sofar
                
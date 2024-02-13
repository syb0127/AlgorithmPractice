class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #this is a dynammic programming question, not a sliding window question
        #I only need to return the sum and not the subarray
        #it would be an overkill for me to keep two pointers - start and end - just keep two integer variables
        #relies on the fact that positive numbers can only help us and negative numbers can only hurt us
        current = nums[0]
        maximum = nums[0]
        
        for num in nums[1:]:
            #this is a DP problem as I am choosing whether to exclude or include the next element
            #I need to decide whether to throwaway what I have so far or keep it
            current  = max(num, current + num)
            maximum = max(maximum, current)
        
        return maximum
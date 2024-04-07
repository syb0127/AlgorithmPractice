class Solution:
    def rob(self, nums: List[int]) -> int:
        #same as the House Robber question but with the fact that I'm dealing with a cycle instead of a list
        if not nums:
             return 0
        if len(nums) == 1:
            return nums[0]
        def robList(nums_list):
            if not nums_list:
                return 0
            #in-place dynammic programming
            rob1 = 0
            rob2 = 0
            #sub-problem: robFrom(i) = max(robFrom(i+1), robFrom(i+2)+nums[i])
            #only these two cases are legit since all houses have positive sum of money and everything from the third house can be "better off" by robbing the first or second house
            # [rob1, rob2, n, n+1, ...]
            for n in nums_list:
                temp = max(rob1+n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(robList(nums[1:]), robList(nums[0:len(nums)-1]))
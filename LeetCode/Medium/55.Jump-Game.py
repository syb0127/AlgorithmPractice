class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''possible = False
        def jump(index):
            nonlocal possible
            if possible:
                return
            if (index == len(nums)-1):
                possible = True
                return
            if (index > len(nums)-1):
                return
            for i in range(1, nums[index]+1):
                jump(index+i)
            return
        jump(0)
        return possible'''
        maximum = 0
        if (nums[0] == 0) and len(nums) > 1 :
            return False
        #max_jump = []
        for i in range(len(nums) - 1):
            if (maximum < i):
                return False
            maximum = max(maximum, i+nums[i])
            #max_jump.append(i+nums[i])
        print(maximum)
        return (maximum >= len(nums)-1)
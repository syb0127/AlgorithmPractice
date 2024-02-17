class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #dp[i] = dp[i-1]+dp[i-2]
        #iterative approach, not recursive
        array_num = []
        if n == 1:
            return 1
        elif n == 2:
            return 2
        array_num.insert(1,1) #instead of using append, use insert since we are inserting an item to a specific INDEX
        array_num.insert(2,2)
        for i in range(n+1):
            if i==1 or i==2:
                continue
            array_num.insert(i,array_num[i-1] + array_num[i-2])
        return array_num[n]
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):  # substring
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
    
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

"""def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(string):
            if len(string) == 0 or len(string) == 1:
                return True
            if string[0] != string[len(string)-1]:
                return False
            return isPalindrome(string[1:len(string)-1])

        def backtrack(subset, index):
            if index == len(s):
                result.append(subset.copy())
                return

            for i in range(index, len(s)):
                print(s[index:i+1])
                if not isPalindrome(s[index:i+1]):
                    continue
                subset.append(s[index:i+1])
                backtrack(subset, index+1)
                subset.pop()
        
        backtrack([], 0)
        return result
        """

"""
# Each path down to child is a partition;
# stop going down tree when no long palindrome.
#        0
#      / | \
#     a aa aab 
#    /   | 
#   a    b
#  /
# b
"""

"""    
         aab
       a aa aab
       a  b
       b
    #each vertical line is a subset(partition)

            aabbccdd
    a aa aab

    #worst case, we would have to explore every node of the tree, but we try to short circuit by stopping whenever we see a non-palindrom node
    pseudocode
    1. We need to come up with all possible substring since backtracking is a brute-force approach and we do need to explore all options at some point. 
    2. We do the same for all the children.
"""
class Solution(object):
    def isPalindrome(self, x):
        length = len(str(x))
        if (str(x)[0] == "-"):
            return False
        position = 0
        for s in str(x):
            if (position >= length/2):
                break
            if (str(x)[position] != str(x)[(length - position-1)]):
                return False
            position += 1
        return True
        
        """
        :type x: int
        :rtype: bool
        """
        
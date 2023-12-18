class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        reverse_x = 0
        if x < 0:
            negative = True
            x = -1 * x
        digits = []
        num_digits = 0
        while x>0:
            num_digits += 1
            digits.append(x%10)
            x = x//10
        for d in digits: 
            reverse_x += d * (10**(num_digits-1))
            num_digits -= 1
        if negative:
            reverse_x *= -1
        if (reverse_x < -2**31) or (reverse_x > 2**31-1):
            return 0
        return reverse_x
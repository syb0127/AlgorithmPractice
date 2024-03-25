class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes = 0
        current_multiple = 5
        while n >= current_multiple: 
            zeroes += n//current_multiple
            current_multiple *= 5
        
        return zeroes
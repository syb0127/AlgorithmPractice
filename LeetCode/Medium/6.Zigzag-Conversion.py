class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # A       A
        # A     A A
        # A   A   A 
        # A A     A 
        # A       A
        # numRows = 5 ; diagonal = 3

        zigzag = [[''] for _ in range(numRows)]
        
        index = 0
        rows = 0
        while index < len(s):

            # straight
            for i in range(numRows):
                zigzag[i].append(s[index])
                index += 1
                if index >= len(s):
                    break
            
            if index >= len(s):
                    break
                    
            # diagonal
            rows = numRows-2
            while rows > 0:
                zigzag[rows].append(s[index])
                rows -= 1
                index += 1
                if index >= len(s):
                    break

        res = ''
        for row in zigzag:
            res += ''.join(row)
        return res
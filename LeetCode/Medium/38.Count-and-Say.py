class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
                
        a= [1]
        for _ in range(1,n):
            i = 0
            new_a = []
            while i < len(a):
                next_num = a[i]
                counter = 0
                while i < len(a) and a[i] == next_num :
                    counter +=1
                    i += 1
                new_a.append(counter)
                new_a.append(next_num)
            a = new_a
        
        return "".join([str(item) for item in a])
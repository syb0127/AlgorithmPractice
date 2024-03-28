class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #sliding window approach using a HashSet
        result = []
        #sequence:count
        seen = {}
        
        if len(s) < 10:
            return result
        
        start, end = 0, 9

        while end <= len(s):
            if s[start:end+1] in seen:
                seen[s[start:end+1]] += 1
            else:
                seen[s[start:end+1]] = 1   
            start += 1
            end +=1             

        for s in seen:
            if seen[s] > 1:
                result.append(s)
        return result

        #Runtime complexity: O((N-L)L)
        #Space complexity: O((N-L)L)
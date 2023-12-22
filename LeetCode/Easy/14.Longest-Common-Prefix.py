class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = 0
        shortest_len = min([len(s) for s in strs])
        for j in range(shortest_len): #character index number
            for i in range(len(strs)): #word index number
                if (strs[i][j] != strs[0][j]):
                    if (j == 0):
                        return ""
                    return strs[0][0:(length)]
            length += 1
        return strs[0][0:(length)]
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(ind, address, dots):
            print(address)
            if dots == 4 and ind == len(s):
                res.append(address[:-1])
                return
            
            for i in range(3):
                if ind+i >= len(s):
                    break
                integer = s[ind:(ind+i+1)]
                if int(integer) <= 255:
                    if dots == 4:
                        return
                    #leading 0
                    if i > 0 and integer[0] == "0":
                        break
                    backtrack(ind+i+1, address+integer+".", dots+1)
            return

        backtrack(0, "", 0)
        return res
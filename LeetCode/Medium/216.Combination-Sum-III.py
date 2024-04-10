class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        final = []

        def backtrack(remaining, combination, ind):
            #don't forget about k!
            if remaining == 0 and len(combination) == k: 
                final.append(list(combination))
                return
            elif remaining < 0 or len(combination) == k:
                return
            
            for i in range(ind+1, 10):
                combination.append(i)
                backtrack(remaining - i, combination, i)
                combination.pop()

        backtrack(n, [], 0)
        return final
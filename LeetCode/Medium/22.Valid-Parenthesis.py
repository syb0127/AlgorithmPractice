class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []
        
        def dfs(combination, num_op, num_cl):
            if len(combination) == 2*n:
                final.append(combination)
                return
            if num_op < n:
                dfs(combination+"(", num_op + 1, num_cl)
            if num_op > num_cl:
                dfs(combination+")", num_op, num_cl+1)
            
        dfs("", 0, 0)
        return final
    
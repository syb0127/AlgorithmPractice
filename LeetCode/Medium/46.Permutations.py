class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        lst = []
        temp_lst = [None for i in range(len(nums))]
        
        def backtrack(cur_lst, remainder_lst, ind):
            if len(remainder_lst) == 0:
                lst.append(cur_lst.copy())
                return
            
            for n in range(len(remainder_lst)):
                cur_lst[ind] = remainder_lst[n]
                backtrack(cur_lst, remainder_lst[:n]+remainder_lst[n+1:], ind+1)
                cur_lst[ind] = None

        backtrack(temp_lst, nums, 0)
        return lst
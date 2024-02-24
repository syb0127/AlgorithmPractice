class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, result):
            res.append(result.copy())

            for j in range(i, len(nums)):
                if  j>i and nums[j]== nums[j-1]:
                    continue
                #include nums[j]
                result.append(nums[j])
                backtrack(j+1, result)

                #don't include nums[j]
                result.pop()

        backtrack(0,[])
        return res
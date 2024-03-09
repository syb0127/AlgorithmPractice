class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        removed_duplicates = set(nums)
        longest_len = 0

        for r in removed_duplicates:
            #constant time lookup(for set)
            if r-1 not in removed_duplicates:
                dummy = r+1
                dummy_len = 1
                while dummy in removed_duplicates:
                    dummy += 1
                    dummy_len += 1
                longest_len = max(longest_len, dummy_len)

        return longest_len
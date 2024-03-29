class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #time complexity: O(n) - .reverse() method takes linear time. We reverse the entire array twice(1st time - the entire array. second time - two subarrays)
        #space complexity: we do this in-place, so no extra space was needed.
        nums.reverse()

        def rotate_sublist(start, end):
            while start < end:
                print(start,end)
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        if k > len(nums):
            k %= len(nums)
        if len(nums) <= 1:
            return nums 
        rotate_sublist(0, k-1)
        rotate_sublist(k, len(nums)-1)
        return nums
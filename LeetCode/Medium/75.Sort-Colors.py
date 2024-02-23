class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end_zero = 0
        start_two = len(nums)-1
        tracker = 0 #what color we are looking at

        while tracker <= start_two:
          #if red(0)
          if nums[tracker] == 0:
            nums[tracker], nums[end_zero] = nums[end_zero], nums[tracker]
            end_zero += 1
            tracker += 1
          #if white(1)
          elif nums[tracker] == 1:
            tracker += 1
          #if blue(2)
          else:
            nums[tracker], nums[start_two] = nums[start_two], nums[tracker]
            start_two -= 1

        return
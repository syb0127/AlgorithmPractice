class Solution:
    def binarySearch(self, lst, left, right):
        if left == right:
            return left
        middle = (left+right)//2
        #determine if we are on rising or falling slope
        #we are using binary search because we are looking for the PEAK
        #this is the case when we are on a falling slope
        if lst[middle] > lst[middle+1]:
            return self.binarySearch(lst, left, middle)
        #rising slope
        return self.binarySearch(lst, middle+1, right)
    
    def findPeakElement(self, nums: List[int]) -> int:
        return self.binarySearch(nums, 0, len(nums)-1)

    #time complexity: O(log n) - reduce the search space in half at every step
    #space complexity: O(log n) - DEPTH OF RECURSION TREE
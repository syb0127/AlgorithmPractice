class Solution:
    pos = -1

    def binarySearch(self, lst, left, right, target, is_starting):
        if left >= right:
            return self.pos
        middle = (left+right)//2
        if lst[middle] == target:
            self.pos = middle
            if is_starting:
                return self.binarySearch(lst, left, middle, target, True)
            else:
                return self.binarySearch(lst, middle+1, right, target, False)
        if lst[middle] < target:
            return self.binarySearch(lst, middle+1, right, target, is_starting)
        if lst[middle] > target:
            return self.binarySearch(lst, left, middle, target, is_starting)


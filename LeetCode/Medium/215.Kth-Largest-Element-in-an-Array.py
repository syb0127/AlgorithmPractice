import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for n in nums:
            heapq.heappush(heap, -1 * n)
        
        final = 0
        for i in range(k-1):
            heapq.heappop(heap)
        final = heapq.heappop(heap) * -1
        return final
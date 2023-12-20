class Solution:
    def maxArea(self, height: List[int]) -> int:
        low_pointer = 0
        high_pointer = len(height)-1
        max_area = 0

        
        while low_pointer < high_pointer:

            new_area = (high_pointer-low_pointer)*(min(height[high_pointer], height[low_pointer]))
            #굳이 max_area랑 new_area 비교 할 필요 없이. max 함수 사용
            max_area = max(max_area, new_area)
            #두 포인터를 한번에 움직이는 것이 아니고 비교를 해서 작은 쪽을 움직이는 것
            if height[low_pointer] <= height[high_pointer]:
                low_pointer += 1
            else:
                high_pointer -= 1
            """
            둘 중 하나만 움직여야 해서 이렇게 하면 안됨
            low_pointer += 1
            high_pointer -= 1
            """
                
        return max_area
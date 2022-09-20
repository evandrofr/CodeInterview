from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        max_left = 0
        max_right= 0
        left = 0
        right = len(height) -1
        
        while left<=right:
            if max_left<=max_right:
                water += max(0,max_left-height[left])
                max_left = max(max_left,height[left])
                left+=1
            else:
                water += max(0,max_right-height[right])
                max_right = max(max_right,height[right])
                right-=1
        return water
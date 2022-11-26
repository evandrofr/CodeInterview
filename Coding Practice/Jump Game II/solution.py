from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0
        right = 0
        counter = 0
        for i in range(len(nums)-1):
            right = max(right, i+nums[i])
            if i == left:
                counter += 1
                left = right
        return counter
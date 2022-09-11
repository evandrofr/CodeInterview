from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, n in enumerate(nums):
            temp = target - nums[idx]
            if temp in dic:
                return [idx, dic[temp]]
            else:
                dic[nums[idx]] = idx
        return []

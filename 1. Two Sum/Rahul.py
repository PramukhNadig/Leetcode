class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumMap = {}
        for i, x in enumerate(nums):
            if x in twoSumMap:
                return [i, twoSumMap[x]]
            else:
                twoSumMap[target - x] = i

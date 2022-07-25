class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSearched = dict()
        
        for i in range(len(nums)):
            if(target - nums[i] in numsSearched):
                return [numsSearched.get(target-nums[i]), i]
            numsSearched[nums[i]] = i
        
        return [-1, -1]

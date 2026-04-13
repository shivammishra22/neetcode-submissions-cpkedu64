class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        predic={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in predic:
                return[predic[diff],i]
            predic[n]=i
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=[-1]*len(nums)

        def dfs(i):
            if(i==0):
                return nums[i]
            if(i<0):
                return 0
            if memo[i] != -1:
                return memo[i]
            else:
                pick=nums[i]+dfs(i-2)
                not_pick=0+dfs(i-1)
                memo[i] = max(pick,not_pick)
                return memo[i]
        return dfs(len(nums)-1)
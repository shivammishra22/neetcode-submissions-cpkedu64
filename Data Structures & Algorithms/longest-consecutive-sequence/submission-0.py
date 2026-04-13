class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        cnt=0
        longest=0
        last_num=float("-inf")
        for i in range(len(nums)):
            num=nums[i]
            if(num-1==last_num):
                cnt+=1
                last_num=num

                
            elif(num!=last_num):
                cnt=1
                last_num=num
            longest=max(longest,cnt)
        return longest





        
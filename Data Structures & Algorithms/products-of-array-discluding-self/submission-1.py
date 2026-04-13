class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        cnt_zero=0
        
        for i in nums:
            if(i==0):
                cnt_zero+=1
            else:
                prod*=i
        res=[]
        if cnt_zero>1:
            return [0]*len(nums)
        
        if cnt_zero==1:
            for i in nums:
                if i==0:
                    res.append(prod)
                else:
                    res.append(0)
            return res
        for i in nums:
            res.append(prod//i)
        return res
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for i in dic:
            if(dic[i]>1):
                return True
        return False
        
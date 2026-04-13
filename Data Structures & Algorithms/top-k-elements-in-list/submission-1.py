class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicmap={}
        l=[[] for i in range(len(nums)+1)]
        for i in nums:
            dicmap[i]=dicmap.get(i,0)+1
        for i,n in dicmap.items():
            l[n].append(i)
        
        res=[]
        for i in range(len(l)-1,0,-1):
            for num in l[i]:
                res.append(num)
                if len(res)==k:
                    return res




        



            


        
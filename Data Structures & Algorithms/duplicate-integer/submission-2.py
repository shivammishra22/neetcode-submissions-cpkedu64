class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicmap={}
        x=1
        for i in (nums): 
            if i in dicmap:
                dicmap[i]+=1
            else:
                dicmap[i]=1
        for i,n in dicmap.items():
            if(n>1):
                x+=1
                break
        if x>1:
            return True
        else:
            return False

            


        
        

        
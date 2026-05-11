class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        cnt=[0]*256
        for i in range(len(s)):
            cnt[ord(s[i])]+=1
            cnt[ord(t[i])]-=1
        for i in cnt:
            if(i>0):
                return False
        return True
        
        
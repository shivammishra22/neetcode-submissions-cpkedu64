class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr=[0]*256
        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            arr[ord(s[i])]+=1
            arr[ord(t[i])]-=1
        for i in arr:
            if(i>0):
                return False
        return True
        
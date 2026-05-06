class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        st=''.join(i.lower() for i in s if i.isalnum())
        l=0
        h=len(st)-1
        for i in range(len(st)):
            if(st[l]==st[h]):
                l+=1
                h-=1
            else:
                return False
        return True


        
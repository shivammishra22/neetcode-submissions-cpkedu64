class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(t==""):
            return ""
        cnt,window={},{}
        
       
        for c in t:
            cnt[c]=1+cnt.get(c,0)
        have=0
        need=len(cnt)
        l=0
        res=[-1,-1]
        reslen=float('infinity')

        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)

            if(c in cnt )and (window[c]==cnt[c]):
                have+=1
            
            while(have==need):
                if(r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                window[s[l]]-=1
                if(s[l] in cnt and window[s[l]]<cnt[s[l]]):
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!=float('infinity') else ""

        



        

        
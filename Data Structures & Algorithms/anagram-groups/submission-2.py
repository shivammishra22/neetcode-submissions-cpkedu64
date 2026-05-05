class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for s in strs:
            cnt=[0]*26
            for char in s:
                cnt[ord(char)-ord('a')]+=1
            key=tuple(cnt)
            if key not in res:
                res[key]=[s]
            else:
                res[key].append(s)
        return list(res.values())

        
        
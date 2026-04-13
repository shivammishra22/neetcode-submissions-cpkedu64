class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            count=[0]*26
            for c in i:
                count[ord(c)-ord('a')]+=1
            key=tuple(count)
            if(key not in dic ):
                dic[key]=[i]
            else:
                dic[key].append(i)
        return list(dic.values())      


        
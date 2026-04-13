class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={')':'(','}':'{',']':'['}
        for i in s:
            if(i in dic):
                if(len(stack)!=0 and stack[-1]==dic[i]):
                    stack.pop()
                else:
                    return False
             

            else:
                stack.append(i)
        if(len(stack)==0):
            return True
        return False

        # return True if not stack else False


        
        
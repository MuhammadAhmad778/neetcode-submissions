class Solution:
    def isValid(self, s: str) -> bool:
        temp=[]
        for i in range(len(s)):
            if s[i]=="["or s[i]=="{"or s[i]=="(":
                temp.append(s[i])
            if s[i]=="]" or s[i]=="}"or s[i]==")":
                if len(temp)!=0:
                    num=temp.pop()
                else:
                    return False
                if (num=="["and s[i]=="]") or (num=="{"and s[i]=="}")or (num=="("and s[i]==")"):
                    continue
                else:
                    return False
        if len(temp)!=0:
            return False             
        return True       
            
          
        
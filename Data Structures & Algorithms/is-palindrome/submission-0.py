class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=[]
        flag=True
        for i in range(len(s)):
            if ("A"<=s[i]<="Z") or("a"<=s[i]<="z") or ("0"<=s[i]<="9"):
                temp.append(s[i])
            
        
        out=len(temp)-1
        for i in range(len(temp)//2):
            if temp[i].lower()!=temp[out].lower():
                return False
            out-=1
        return True
           




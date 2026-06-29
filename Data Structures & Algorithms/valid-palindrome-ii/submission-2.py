class Solution:
    def checker(self,S:str)->bool:
        out=len(S)-1
        for i in range(len(S)//2):
            if S[i]!=S[out]:
                return False
            out-=1
        return True


    def validPalindrome(self, s: str) -> bool:
        out=len(s)-1
        for i in range(len(s)//2):
            if  s[i]!=s[out]:
                if self.checker(s[:i]+s[i+1:]) or self.checker(s[:out]+s[out+1:]):
                    return True
                else:
                    return False
            out-=1
        return True
     
        
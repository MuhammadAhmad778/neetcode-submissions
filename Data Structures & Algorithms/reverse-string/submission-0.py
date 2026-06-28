class Solution:
    def reverseString(self, s: List[str]) -> None:
        out=len(s)-1
        for i in range(len(s)//2):
            temp=s[i]
            s[i]=s[out]
            s[out]=temp
            out=out-1

       
        
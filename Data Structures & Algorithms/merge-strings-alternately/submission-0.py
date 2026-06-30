class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        c1,c2=0,0
        res=""
        while l1!=0 and l2!=0:
            res+=(word1[c1]+word2[c2])
            c1+=1
            c2+=1
            l1-=1
            l2-=1
        if l1==0 and l2!=0:
            res+=word2[c2:]

        if l2==0 and l1!=0:
            res+=word1[c1:]
        return res


        
       

        
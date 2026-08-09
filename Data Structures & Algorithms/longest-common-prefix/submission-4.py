class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=strs[0]
      
        for i in range(1,len(strs)):
            count=0
            temp=strs[i]
            while count<len(res) and count<len(temp) and res[count]==temp[count]:
                count+=1
            res=res[:count]
        if res=="":
            return ""
        else:
            return res



        
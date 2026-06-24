class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
           pre=strs[0]
           
           for j in range(1,len(strs)):
            i=0
            
            while(i<len(pre) and i<len(strs[j])):
                if pre[i]!=strs[j][i]:
                    break
                i=i+1
            

            pre=pre[:i]

        if pre=="":
                return ""

        return pre
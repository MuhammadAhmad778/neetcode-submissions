class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            char = ""

        t1 = ""
        t2 = ""

        t1 = strs[0]
        t2 = strs[1]
        i = 0

        while i < len(t1) and i < len(t2):
            if t1[i] != t2[i]:
                break
            if char == "":
                char = t1[i]
            else:
                char += t1[i]
            i = i + 1

        if char == "":
            return ""

        for j in strs:
            x = len(char)
            i = 0

            while x != 0 and i<len(j) :
                if j[i] == char[i]:
                    x = x - 1
                else:
                    break
                i = i + 1

            char = char[:i]

        return char
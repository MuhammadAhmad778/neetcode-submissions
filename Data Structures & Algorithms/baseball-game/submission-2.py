class Solution:
    def calPoints(self, operations: List[str]) -> int:
        cal=[]
        count=0
        for i in range(len(operations)):
            if operations[i]!="+" and operations[i]!="D" and operations[i]!="C":
                cal.append(int(operations[i]))
                count+=1
            else:
                if operations[i]=="+":
                    cal.append(int(cal[count-2]) + int(cal[count-1]))
                    count+=1
                elif operations[i]=="D":
                    cal.append(2*cal[count-1])
                    count+=1
                else:
                    cal.pop()
                    count-=1
        Sum=0
        for i in cal:
            Sum+=int(i)
        return Sum

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        temp=Counter(arr)
        largest=-1
        for c,n in temp.items():
            if c==n:
                largest=max(largest,c)
        return largest
        
        
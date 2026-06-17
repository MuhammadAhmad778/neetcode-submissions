class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x=len(nums)
        ans=[]
        ans=[0]*(2*x)
        for i in range(len(nums)):
            ans[i]=nums[i]
        for j in range( len(nums)):
            ans[j+x]=nums[j]
        return ans
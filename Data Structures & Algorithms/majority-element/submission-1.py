class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums=sorted(nums)
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        else:
            return nums[len(nums)//2]
           
          
      
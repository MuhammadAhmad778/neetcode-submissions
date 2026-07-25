class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        x=set()
        l=0

        for r in range(len(nums)):
            if r-l >k:
                x.remove(nums[l])
                l+=1
            if nums[r] in x:
                return True
            x.add(nums[r])
        
        return False

        
       
    
       

        
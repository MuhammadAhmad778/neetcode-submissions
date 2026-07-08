class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        mid = len(nums)//2
        
        if nums[mid]==target:
            return mid
        else:
            if nums[mid]<target:
                    return mid+ 1 + self.search(nums[mid + 1:],target)
            else:
                 return self.search(nums[:mid],target)

        
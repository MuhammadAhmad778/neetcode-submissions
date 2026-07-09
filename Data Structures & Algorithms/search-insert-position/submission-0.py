class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid=len(nums)//2
        if not nums:
            return 0

        if nums[mid]==target:
            return nums.index(target)
        if nums[mid]<target:
            return mid + 1 + self.searchInsert(nums[mid+1:],target)
        else:
            return self.searchInsert(nums[:mid],target)

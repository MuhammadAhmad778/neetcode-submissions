class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp=set()
        i=0
        while True:
            if i>=len(nums):
                break
            if nums[i] not in temp:
                temp.add(nums[i])
                i+=1
            else:
                del nums[i]
                continue
        return len(nums)




      
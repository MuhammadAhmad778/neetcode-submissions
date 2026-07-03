class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        count=0
        if len(nums1)!=(m+n):
            return
        else:
            for i in range(m,len(nums1)):
                nums1[i]=nums2[count]
                count=count+1
            nums1.sort()
            return

        
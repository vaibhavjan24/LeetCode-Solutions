class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        n1=len(nums1)
        n2=len(nums2)
        ans=[]
        i=0
        j=0
        while i<n1 and j<n2:
            if nums1[i]==nums2[j]:
                ans.append(nums1[i])
                i=i+1
                j=j+1
            elif nums1[i]>nums2[j]:
                j=j+1
            else:
                i=i+1
        return ans
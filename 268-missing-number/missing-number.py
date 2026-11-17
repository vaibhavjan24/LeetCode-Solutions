class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        biggest=0
        for i in range(n):
            if nums[i]>biggest:
                biggest=nums[i]
        if n==biggest:    
            s1=n*(n+1)//2
            s2=0
            for j in range(n):
                s2=s2+nums[j]
            diff=s1-s2
        elif biggest<n:
            diff=n
        return diff
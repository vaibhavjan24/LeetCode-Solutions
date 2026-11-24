class Solution:
    def search(self, nums: list[int], target: int) -> int:
        head=0
        tail=len(nums)-1
        while head<=tail:
            mid=(head+tail)//2
            if target>nums[mid]:
                head=mid+1
            elif target<nums[mid]:
                tail=mid-1
            else:
                return mid
        return -1
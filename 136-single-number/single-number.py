class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        mySet=set()
        for i in range(len(nums)):
            if nums[i] in mySet:
                mySet.remove(nums[i])
            else:
                mySet.add(nums[i])
        return int(list(mySet)[0])

#class Solution:
#    def singleNumber(self, nums: list[int]) -> int:
#        res = 0
#        for num in nums:
#            res ^= num
#        return res
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            num=str(x)
            l=len(num)
            for i in range((l//2)+1):
                if num[i]!=num[l-i-1]:
                    return False
            return True
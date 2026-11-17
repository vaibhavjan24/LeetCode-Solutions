class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x=num
        while True:
            if x*x==num:
                return True
            elif x*x>num:
                x=x//2
            else:
                start=x
                end=2*x
                while start<=end:
                    mid=(start+end)//2
                    if mid*mid==num:
                        return True
                    elif mid*mid<num:
                        start=mid+1
                    else:
                        end=mid-1
                return False

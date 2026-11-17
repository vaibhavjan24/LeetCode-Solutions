class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        
        else:
            a=1
            b=2
            for i in range(2,n):
                t=b
                b=b+a
                a=t
            return b
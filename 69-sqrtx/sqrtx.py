class Solution:
    def mySqrt(self, x: int) -> int:
        y=x
        while True:
            if y*y==x:
                return y
            elif y*y>x:
                y=y//2
            else:
                while y*y<x:
                    y=y+1
                if y*y==x:
                    return y
                else:
                    return y-1
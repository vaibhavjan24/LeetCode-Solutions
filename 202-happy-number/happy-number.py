class Solution:
    def isHappy(self, n: int) -> bool:

        def split(n):
            l = len(str(n))
            arr=[]
            quotient=n
            for i in range(l):
                quotient=quotient//10**(l-i-1)
                arr.append(quotient)
                remainder=n%10**(l-i-1)
                quotient=remainder
            return arr

        def sum(arr):
            l=len(arr)
            s=0
            for i in range(l):
                s=s+arr[i]**2
            return s

        mySet=set()
        while True:
            x=sum(split(n))
            if x==1:
                return True
            else:
                if x in mySet:
                    return False
                else:
                    mySet.add(x)
                    n=x
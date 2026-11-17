class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=len(s)
        j=l-1
        count=0
        while s[j]==' ':
            j=j-1
        i=j
        while i>=0:
            if s[i]!=' ':
                i=i-1
                count=count+1
            else:
                return count
        return count
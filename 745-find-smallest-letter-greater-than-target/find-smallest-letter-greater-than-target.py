class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for i in range(len(letters)-1):
            if target<letters[i]:
                return letters[i]
        if letters[-1]>target:
            return letters[-1]
        else:
            return letters[0]
        
#        if letters[len(letters)-1]<target or letters[len(letters)-1]==target:
#            return letters[0]
#        elif letters[len(letters)-1]>target:
#            return letters[len(letters)-1]
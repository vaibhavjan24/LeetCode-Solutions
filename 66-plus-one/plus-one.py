class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n=len(digits)
        pointer=n-1
        while pointer >= 0:
            if digits[pointer]!=9:
                digits[pointer]=digits[pointer]+1
                return digits
            else:
                while digits[pointer]==9 or pointer<0:
                    if digits[pointer]==9:
                        digits[pointer]=0
                        pointer=pointer-1
                    else:
                        digits.insert(0,1)
                        return digits
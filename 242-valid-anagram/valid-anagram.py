class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def machine(string):
            dictionary={}   # value -> count
            for ch in string:
                if ch in dictionary:
                    dictionary[ch]=dictionary[ch]+1
                else:
                    dictionary[ch]=1
            return dictionary

        if machine(s)==machine(t):
            return True
        else:
            return False
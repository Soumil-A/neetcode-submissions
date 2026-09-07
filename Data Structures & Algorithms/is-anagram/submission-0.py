class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        
        for i in range(len(s)):
            # .get() prevents KeyErrors by defaulting the count to 0 if the character is new
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        # Dictionaries in Python can be directly compared for equality
        return countS == countT
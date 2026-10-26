class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charS = {}
        charT = {}
        for char in s:
            if char in charS:
                charS[char] += 1
            else:
                charS[char] = 1
        for char in t:
            if char in charT:
                charT[char] += 1
            else:
                charT[char] = 1
        return charS == charT
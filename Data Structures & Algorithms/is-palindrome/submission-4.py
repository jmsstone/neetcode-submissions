class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        if not s:
            return True
        validc = "abcdefghijklmnopqrstuvwxyz0123456789"
        while left < right:
            while left < right and s[left].lower() not in validc:
                left += 1
            while left < right and s[right].lower() not in validc:
                right -= 1
            if right <= left:
                return True
            else:
                if s[left].lower() == s[right].lower():
                    right -= 1
                    left += 1
                else:
                    return False
        return True
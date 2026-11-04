class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while n != 1:
            temp = 0
            while n != 0:
                temp += (n % 10)**2
                n = n // 10
            n = temp
            if n in seen:
                return False
            seen.append(n)
        return True
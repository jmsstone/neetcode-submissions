class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s)) + "#" + s
        print(ret)
        return ret
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        state = True
        num = ""
        while i < len(s):
            if s[i] == "#":
                val = int(num)
                strs.append(s[i+1:i+val+1])
                i += val + 1
                state = True
                num = ""
                continue
            if state == True:
                num += s[i]
            i += 1
        return strs

            

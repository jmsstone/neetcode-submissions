class Solution:
    def createCharDict(self,string:str):
        counts = [0]*26
        for char in string:
            counts[ord(char) - ord('a')] += 1
        return counts
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        res = {}
        for string in strs:
            anagrams.append(self.createCharDict(string))
        for i in range(len(anagrams)):
            index = tuple(anagrams[i])
            if index in res:
                res[index].append(strs[i])
            else:
                res[index] = [strs[i]]
        return list(res.values())

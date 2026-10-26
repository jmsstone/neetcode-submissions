class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        vals = list(freqs.keys())
        vals.sort(reverse = True, key=freqs.get)
        return vals[:k]
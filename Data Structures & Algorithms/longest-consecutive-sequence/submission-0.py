class Solution:
    def followRoot(self, root, outs):
        count = 1
        while (1):
            if len(outs[root]) > 0:
                count += 1
                root = outs[root][0]
            else:
                break
        return count 
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ins = {}
        outs = {}
        for n in nums:
            ins[n] = []
            outs[n] = []
        for n in nums:
            if n+1 in ins:
                ins[n+1].append(n)
        for n in nums:
            if n-1 in outs:
                outs[n-1].append(n)
        roots = []
        for num in ins:
            if len(ins[num]) == 0:
                roots.append(num)
        
        return max(self.followRoot(root, outs) for root in roots)
        

        
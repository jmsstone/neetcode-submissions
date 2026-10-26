class Solution:
    def leftProd(self, nums: List[int]):
        leftPrefixProds = []
        prod = 1
        for num in nums:
            prod = prod * num
            leftPrefixProds.append(prod)
        return leftPrefixProds
    def rightProd(self, nums: List[int]):
        rightPrefixProds = []
        prod = 1
        for num in nums[::-1]:
            prod = prod * num
            rightPrefixProds.append(prod)
        return rightPrefixProds
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = []
        lefts = self.leftProd(nums)
        rights = self.rightProd(nums)[::-1]
        for i in range(len(nums)):
            if (i == 0):
                prods.append(rights[i+1])
            elif (i == len(nums)-1):
                prods.append(lefts[i-1])
            else:
                prods.append(lefts[i-1]*rights[i+1])
        return prods
        
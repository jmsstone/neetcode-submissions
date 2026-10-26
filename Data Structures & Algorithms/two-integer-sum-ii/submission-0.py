class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lpointer = 0
        rpointer = len(numbers)-1
        while (1):
            if numbers[rpointer] > target-numbers[lpointer]:
                rpointer -= 1
            if numbers[rpointer] < target-numbers[lpointer]:
                lpointer += 1
            if numbers[rpointer] == target-numbers[lpointer]:
                return [lpointer+1,rpointer+1]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        InMap = {}
        for ch, n in enumerate(nums):
            diff = target - n
            if diff in InMap:
                return [InMap[diff],ch]
            InMap[n] = ch
        else:
            return False


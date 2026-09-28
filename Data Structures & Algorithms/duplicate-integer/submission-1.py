class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = set()
        for ch in nums:
            if ch not in map:
                map.add(ch)
            else:
                return True
        return False
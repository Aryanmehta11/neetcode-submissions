class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashed_set=set()
        for n in nums:
            if n in hashed_set:
                return True
            hashed_set.add(n)
        return False       
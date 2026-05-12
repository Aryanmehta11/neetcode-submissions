class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashed_set=set()
        for num in nums:
            if num in hashed_set:
                return True
            hashed_set.add(num)  
        return False     
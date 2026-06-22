class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group={}
        for num in nums:
            group[num]=group.get(num,0)+1

        sorted_freq=sorted(
            group.items(),
            key=lambda x:x[1],
            reverse=True
        )        

        result=[]
        for num,count in sorted_freq[:k]:
            result.append(num)
        return result    
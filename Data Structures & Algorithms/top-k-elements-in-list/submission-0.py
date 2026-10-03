from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = defaultdict(int)

        for num in nums:
            data[num] += 1
        
        sorted_data_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

        result = list(sorted_data_desc.keys())
        
        return result[0:k]
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map={}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        sorted_keys = sorted(freq_map, key=freq_map.get)
        sorted_keys.reverse()

        return sorted_keys[:k]
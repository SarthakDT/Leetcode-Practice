class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        missing = []

        for i in range(1, 2001):
            if i not in arr_set:
                missing.append(i)

        return missing[k-1]

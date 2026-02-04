class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing=[]

        for i in range(1,2001):
            missing.append(i)
        
        i = 0

        while i < len(missing):
            if missing[i] in arr:
                missing.pop(i)
            else:
                i += 1

        return missing[k-1]

            
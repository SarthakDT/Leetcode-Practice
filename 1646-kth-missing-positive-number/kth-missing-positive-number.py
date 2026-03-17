class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num=1
        count=0

        arr_set=set(arr)

        while True:
            if num not in arr_set:
                count+=1
            
            if count==k:
                return num
            
            num+=1

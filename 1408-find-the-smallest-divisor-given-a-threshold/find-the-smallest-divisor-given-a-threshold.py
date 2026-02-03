class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        l = 1
        r = max(nums)

        while l <= r:
            mid = l + (r - l) // 2
            total = 0

            for i in range(n):
                total += (nums[i] + mid - 1) // mid

            if total <= threshold:
                r = mid - 1
            else:
                l = mid + 1

        return l
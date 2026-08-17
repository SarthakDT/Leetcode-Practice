class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = -1

        top = 0
        bottom = len(matrix)-1

        while top<=bottom:
            mid_row=(top+bottom)//2

            if matrix[mid_row][0] <= target and target <= matrix[mid_row][-1]:
                m=mid_row
                break

            elif target<matrix[mid_row][0]:
                bottom = mid_row-1
            
            elif target>matrix[mid_row][-1]:
                top = mid_row+1

        if m == -1:
            return False

        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[m][mid] == target:
                return True

            elif matrix[m][mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return False    
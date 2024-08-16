class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if (arr[i] == 0):
                arr.insert(i+1, 0)
                arr.pop()
                i = i+2
            else:
                i = i+1


sol = Solution()
arr = [0, 1, 7, 6, 0, 2, 0, 7]
sol.duplicateZeros(arr)

print(arr)

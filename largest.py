class Solution:
    def findKthLargest(self, arr, k):
        left = 0
        right = len(arr) - 1
        while left <= right:
            pivotIndex = self._partition(arr, left, right)
            if pivotIndex == len(arr) - k:
                return arr[pivotIndex]
            elif pivotIndex > len(arr) - k:
                right = pivotIndex - 1
            else:
                left = pivotIndex + 1
        return -1

    def _partition(self, arr, low, high):
        pivot = arr[high]
        index = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[index], arr[j] = arr[j], arr[index]
                index += 1
        arr[index], arr[high] = arr[high], arr[index]
        return index


input = [10, 14, 4, 6, 8, 2, 12]
print(Solution().findKthLargest(input, 3))
# 10

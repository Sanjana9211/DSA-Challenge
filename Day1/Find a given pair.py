class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        arr.sort()
        i, j = 0, 1
        while i < n and j < n:
            diff = arr[j] - arr[i]
            if diff == x and i != j:
                return 1
            elif diff < x:
                j += 1
            else:
                i += 1
        return -1
        


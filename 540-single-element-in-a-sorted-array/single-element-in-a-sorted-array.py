class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if mid % 2 == 1:
                mid -= 1
            if(arr[mid] == arr[mid + 1]):
                l = mid + 2
            else:
                r = mid
        return(arr[l])

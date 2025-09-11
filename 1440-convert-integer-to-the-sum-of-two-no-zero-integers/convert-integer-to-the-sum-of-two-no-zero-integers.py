class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def zero(y):
            return '0' not in str(y) 
        
        for i in range(n):
            a = n - i
            if zero(a) and zero(i):
                return [i, a]
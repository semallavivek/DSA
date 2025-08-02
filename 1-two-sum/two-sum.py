class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dici = {}

        for i, num in enumerate(nums):
            if num in dici:
                return((dici[num], i))
                break
            else:
                dici[target - num] = i
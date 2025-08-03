class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        l_p = 1
        r_p = 1

        for i in range(len(nums)):
            result[i] = l_p
            l_p *= nums[i]

        for i in reversed(range(len(nums))):
            result[i] *= r_p
            r_p *= nums[i]

        return(result)
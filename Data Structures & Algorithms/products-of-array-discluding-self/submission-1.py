class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_list = len(nums)
        pref_prod = [1] * len(nums)
        suff_prod = [1] * len(nums)

        pref_prod[1] = nums[0]
        for i in range(1, len_list):
            pref_prod[i] = pref_prod[i-1] * nums[i-1]

        suff_prod[-2] = nums[-1]
        for i in range(len_list-2, -1, -1):
            suff_prod[i] = suff_prod[i+1] * nums[i+1]
        
        sol = [1] * len(nums)
        for i in range(len_list):
            sol[i] = pref_prod[i] * suff_prod[i]
        
        
        return sol
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        len_nums = len(nums)
        for i in range(len_nums):
            dic[nums[i]] = i
        
        for i in range(len_nums):
            j = dic.get(target-nums[i])
            if j is not None and j!=i:
                return [i, j]

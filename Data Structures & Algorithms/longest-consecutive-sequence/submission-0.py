class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = True
        
        max_num = nums[0]
        for num in nums:
            if max_num < num:
                max_num = num

        count = 0
        for i in range(len(nums)):
            temp_cnt = 1
            for search_num in range(nums[i]+1, max_num+1):
                if dic.get(search_num, False):
                    temp_cnt += 1
                    if temp_cnt > count:
                        count = temp_cnt
                else:
                    temp_cnt = 1
                
                      
        return count
        
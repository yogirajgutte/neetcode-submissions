class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dic = {}
        for num in nums:
            dic[num] = True
        
        max_num = nums[0]
        for num in nums:
            if max_num < num:
                max_num = num

        count = 1
        for num in dic.keys():
            
            temp_cnt = 1
            if not dic.get(num - 1, False):
                for search_num in range(num+1, max_num+1):
                    if dic.get(search_num, False):
                        temp_cnt += 1
                        if temp_cnt > count:
                            count = temp_cnt
                    else:
                        temp_cnt = 1
                        break
                
                      
        return count
        
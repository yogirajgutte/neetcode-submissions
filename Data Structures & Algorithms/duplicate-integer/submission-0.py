class Solution:
    def __init__(self):
        self.freq = {}

    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if self.freq.get(num) is None:
                self.freq[num] = 1
            else:
                return True
        return False


        
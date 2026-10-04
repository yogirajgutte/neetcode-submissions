class Solution:
    def __init__(self):
        self.numSet = {}

    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if self.numSet.get(num):
                return True
            else:
                self.numSet.add(num)
        return False


        
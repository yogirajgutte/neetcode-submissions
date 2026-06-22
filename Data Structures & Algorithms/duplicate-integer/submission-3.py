class Solution:
    def __init__(self):
        self.numSet = set()

    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if num in self.numSet:
                return True
            else:
                self.numSet.add(num)
        return False


        
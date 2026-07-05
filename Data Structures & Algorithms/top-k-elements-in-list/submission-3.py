class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()

        for num in nums:
            if freq_dict.get(num):
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        freq_matrix = [list() for i in range(len(nums) + 1)]

        for num, freq in freq_dict.items():
            freq_matrix[freq].append(num)

        top_k = []
        i = len(freq_matrix) - 1
        while len(top_k) < k:
            if i <= 0:
                top_k = []
            if len(freq_matrix[i]) > 0:
                top_k.extend(freq_matrix[i])
            i -= 1
        
        return top_k
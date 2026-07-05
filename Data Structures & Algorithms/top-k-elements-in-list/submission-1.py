class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        reverse_freq = dict()
        for num in nums:
            if freq.get(num):
                freq[num] += 1
            else:
                freq[num] = 1

        for num in freq.keys():
            count = freq[num]
            if reverse_freq.get(count):
                reverse_freq[count].append(num)
            else:
                reverse_freq[count] = [num]

        sorted_keys = sorted(list(reverse_freq.keys()), reverse=True)

        top_k = []
        i = 0
        while len(top_k)<k:
            top_k.extend(reverse_freq[sorted_keys[i]])
            i += 1
        
        return top_k
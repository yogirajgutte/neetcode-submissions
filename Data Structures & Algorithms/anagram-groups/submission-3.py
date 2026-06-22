class Solution:
    def isAnagram(self, str_1: str, str_2: str) -> bool:
        if len(str_1) != len(str_2):
            return False

        freq = [0] * 26
        str_len = len(str_1)
        for i in range(str_len):
            freq[ord(str_1[i]) - 97] += 1
            freq[ord(str_2[i]) - 97] -= 1
        
        for i in freq:
            if i!=0:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        determined = [0] * len(strs)

        length = len(strs)
        group_lis = []
        for i in range(length):
            if determined[i]:
                continue
            group = [strs[i]]
            for j in  range(i + 1, length):
                if self.isAnagram(strs[i], strs[j]) and determined[j] == 0:
                    group.append(strs[j])
                    determined[j] = 1
                    determined[i] = 1
            group_lis.append(group)
        
        return group_lis
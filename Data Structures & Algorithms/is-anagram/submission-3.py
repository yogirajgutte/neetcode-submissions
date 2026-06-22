class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        str_len = len(s)
        freq = [0]*26
        for i in range(str_len):
            freq[ord(s[i])-97] += 1
            freq[ord(t[i])-97] -= 1
        
        for i in freq:
            if i != 0:
                return False
        return True

        
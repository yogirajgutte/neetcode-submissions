class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache_1 = {}
        cache_2 = {}

        if len(s) != len(t):
            return True

        str_len = len(s)
        for i in range(str_len):
            if cache_1.get(s[i]) is None:
                cache_1[s[i]] = 1
            else:
                cache_1[s[i]] += 1
            
            if cache_2.get(t[i]) is None:
                cache_2[t[i]] = 1
            else:
                cache_2[t[i]] += 1
        
        chars = [chr(x) for x in range(ord('a'), ord('z')+1)]
        for char in chars:
            if cache_1.get(char) != cache_2.get(char):
                return False
        
        return True
        
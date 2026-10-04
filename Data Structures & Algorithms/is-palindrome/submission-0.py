class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1

        while i < j:
            if not self.isAlphanumeric(s[i]):
                i += 1
                continue
            if not self.isAlphanumeric(s[j]):
                j -= 1
                continue
            print(s[i], s[j])
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True
    
    def isAlphanumeric(self, c: str) -> bool:
        if ((ord('A') <= ord(c[0]) <= ord('Z')) or (ord('a') <= ord(c[0]) <= ord('z')) or (ord('0') <= ord(c[0]) <= ord('9'))):
            return True
        else:
            return False


            
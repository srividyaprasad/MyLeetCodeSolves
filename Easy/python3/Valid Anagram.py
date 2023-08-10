class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqarr = dict()
        for i in range(97,123):
            freqarr[i]=0
        for char in s:
            freqarr[ord(char)] = freqarr[ord(char)] + 1

        for char in t:
            if freqarr[ord(char)] == 0:
                return False
            freqarr[ord(char)] -= 1
        return True

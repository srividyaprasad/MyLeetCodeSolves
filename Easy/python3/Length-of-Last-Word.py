class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip()[::-1]
        len = 0
        for ch in s1:
            if(ch==' '):
                break
            len+=1
        return len

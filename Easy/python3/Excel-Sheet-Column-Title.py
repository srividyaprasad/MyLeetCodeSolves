class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        strcol=""
        while(columnNumber!=0):
            columnNumber-=1
            rem=columnNumber%26
            strcol+=str((chr(rem+65)))
            columnNumber//=26
        return strcol[::-1]

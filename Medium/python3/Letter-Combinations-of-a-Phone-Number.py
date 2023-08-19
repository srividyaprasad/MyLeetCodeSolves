class Solution:
    def letterCombinations(self, digits: str) -> List[str]: #23
        li=["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if (len(digits)==0):
            return []
        elif (len(digits)==1):
            return list(li[int(digits[0])-2])
        else:
            ls=[]
            mid=len(digits)//2
            firhalf=list(self.letterCombinations(digits[:mid]))
            sechalf=list(self.letterCombinations(digits[mid:]))
            for digf in firhalf:
                for digs in sechalf:
                    ls.append(digf+digs)
            return ls

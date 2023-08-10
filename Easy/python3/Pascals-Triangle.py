class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        largelist=list()
        for i in range(numRows):
            smalllist=list()
            for j in range(i+1):
                smalllist.append(factorial(i)//(factorial(i-j)*factorial(j)))
            largelist.append(smalllist)
        return largelist

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in digits:
            num=num*10+i
        num+=1
        lsnum = list()
        while(num!=0):
            lsnum.append(num%10)
            num//=10
        return lsnum[::-1]

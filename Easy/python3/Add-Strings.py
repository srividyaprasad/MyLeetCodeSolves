class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len1=len(num1)
        len2=len(num2)
        if(len1-len2>0):
            num2 = ("0"*(len1-len2))+num2
        if(len2-len1>0):
            num1 = ("0"*(len2-len1))+num1
        num1 = num1[::-1]
        num2 = num2[::-1]
        car=0
        strsum=""
        for i in range(len(num1)):
            summ = int(num1[i])+int(num2[i])+car
            if(summ>9):
                car=1
                summ=summ%10
            else:
                car=0
            strsum+=(str(summ))
        if(car==1):
            strsum+="1"
        return strsum[::-1]

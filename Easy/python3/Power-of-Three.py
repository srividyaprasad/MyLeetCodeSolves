import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<=0):
            return False
        else:
            return math.log(n, 3)%1==0 or math.log(n,3)%1>0.999999999999

class Solution:
    def intToRoman(self, num: int) -> str:
        D = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        roman=""
        for n in D:
            if(num>=n):
                roman+=str(D[n]*int(num//n))
                num=num-(n*int(num//n))
        return roman

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ls=list()
        for i in range(1, n+1):
            if(i%3==0 and i%5==0):
                ls.append("FizzBuzz")
            elif(i%3==0):
                ls.append("Fizz")
            elif(i%5==0):
                ls.append("Buzz")
            else:
                ls.append(str(i))
        return ls

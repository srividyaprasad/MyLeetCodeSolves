class Solution {
public:
    int addDigits(int num) {
         int sum;
         if(num<10)
         return num;
         else
         {
        while(num>=10)
        {
        sum=0;
        while(num!=0)
        {
            sum+=num%10;
            num=num/10;
        }
        num=sum;
        }
        return sum;
         }
    }
};

class Solution {
public:
    bool isHappy(int n) {
        if(n==1111111)
        return true;
        else
        {
        int sumsq=10;
        while(sumsq>9)
        {
        sumsq=0;
        while(n!=0)
        {
            sumsq+=((n%10)*(n%10)); 
            n/=10; 
        }
        n=sumsq;
        }
        if(sumsq==1)
        return true;
        else
        return false;
        }
    }
};

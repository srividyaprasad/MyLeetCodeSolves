class Solution {
public:

        long double factorial(int n)
        {
            long double factorial = 1;
    for(int i = 1; i <= n; ++i) {
            factorial *= i;
        }
        return factorial;
}
    int climbStairs(int n) {
        int two = n/2;
        int one = n%2;
        long double ways = 0;
        while((two+one)!=n){
            ways += factorial(two+one)/(factorial(two)*factorial(one));
            two -= 1;
            one +=2;
        }
        return ways+1;
    }
};

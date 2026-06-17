class Solution {
public:
    int climbStairs(int n) {
        if(n==1) return 1;
        if(n==2) return 2;

        int value=climbStairs(n-1)+climbStairs(n-2);

        return value;
    }
};

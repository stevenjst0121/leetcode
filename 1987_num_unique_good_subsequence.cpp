class Solution {
public:
    int numberOfUniqueGoodSubsequences(string binary) {
        // [MEMO] Brilliant DP solution
        // Trick is to count good subsequences ends in 0 and 1 separately
        // '0' needs to be counted separately
        int mod = 1e9 + 7, dp[2] = {0, 0};
        bool has_zero = false;
        for (auto& c : binary) {
            if (c == '0') {
                dp[0] = dp[0] + dp[1];
                has_zero = true;
            } else if (c == '1') {
                dp[1] = dp[0] + dp[1] + 1;
            }
        }
        
        return (dp[0] + dp[1] + has_zero) % mod;
    }
};
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        /**
         * DP
         * [MEMO] Can be applied to longest increasing subsequence
         */
        vector<vector<int>> dp;
        int n = text1.length(), m = text2.length();
        for (int i = 0; i < n; ++i) {
            dp.emplace_back(m, 0);
        }

        for (int i = n - 1; i >= 0; --i) {
            for (int j = m - 1; j >= 0; --j) {
                if (text1[i] == text2[j]) {
                    if (i == n - 1 || j == m - 1) {
                        dp[i][j] = 1;
                    } else {
                        dp[i][j] = dp[i + 1][j + 1] + 1;
                    }
                } else {
                    if (i != n - 1 && j != m - 1) {
                        dp[i][j] = max(dp[i][j + 1], dp[i + 1][j]);
                    } else if (i != n - 1) {
                        dp[i][j] = dp[i + 1][j];
                    } else if (j != m - 1) {
                        dp[i][j] = dp[i][j + 1];
                    }
                }
            }
        }
        return dp[0][0];
    }
};
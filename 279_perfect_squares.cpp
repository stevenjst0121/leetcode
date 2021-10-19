#include <cmath>
#include <deque>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:
    int numSquares(int n) {
        // DP, O(n * sqrt(n))
        vector<int> squares = {1};
        int dp[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i <= n; ++i) {
            // Add perfect squares if needed
            if (static_cast<int>(sqrt(i)) > static_cast<int>(sqrt(squares.back()))) {
                squares.push_back(i);
            }

            // Find min
            int minnum = INT_MAX;
            for (auto square : squares) {
                if (i - square < 0) {
                    break;
                }

                minnum = min(minnum, 1 + dp[i - square]);
            }
            dp[i] = minnum;
        }

        return dp[n];
    }
};

class Solution {
public:
    int numSquares(int n) {
        // [MEMO] Greedy on count
        // Good thinking, but unfortunately still exceeded time limit
        // Memoization does not seem to help much here either
        for (int i = 1; i <= n; ++i) {
            d_squares.push_back(i * i);
        }

        int count = 1;
        for (; count <= n; ++count) {
            if (isDividedBy(n, count)) {
                return count;
            }
        }
        return count;
    }
    bool isDividedBy(int n, int count) {
        if (n == 0 && count == 0) {
            return true;
        }

        if (n <= 0 || count <= 0) {
            return false;
        }

        for (auto square : d_squares) {
            if (isDividedBy(n - square, count - 1)) {
                return true;
            }
        }

        return false;
    }

private:
    vector<int> d_squares;
};

class Solution {
public:
    int numSquares(int n) {
        // [MEMO] BFS + N-ary tree
        // The above greedy solution is basically a BFS on an N-array tree,
        // where N is sqrt(N) - the number of perfect squares
        for (int i = 1; i <= sqrt(n); ++i) {
            d_squares.insert(i * i);
        }

        deque<int> queue = {n};
        int level = 1;
        while (level <= n) {
            int size = queue.size();
            for (int i = 0; i < size; ++i) {
                int res = queue.front();
                queue.pop_front();
                if (d_squares.find(res) != d_squares.end()) {
                    return level;
                }

                // Not found, form next level leaves
                for (auto square : d_squares) {
                    if (res - square > 0) {
                        queue.push_back(res - square);
                    }
                }
            }
            ++level;
        }

        return level;
    }

private:
    set<int> d_squares;
};

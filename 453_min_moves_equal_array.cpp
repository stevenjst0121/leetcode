#include <vector>

using namespace std;

class Solution {
public:
    int minMoves(vector<int>& nums) {
        /**
         * [MEMO]
         * sort and add all diffs, see solution for explanation
         */
        sort(nums.begin(), nums.end());
        int moves = 0;
        for (int i = nums.size() - 1; i > 0; --i) {
            moves += nums[i] - nums[0];
        }
        return moves;
    }

    int minMoves(vector<int>& nums) {
        /**
         * [MEMO]
         * sort and then dp
         * dp thinking is simple, if all elements until i - 1 are the same,
         * then only takes diff to make all elements until i equal. Keep track
         * of moves so far
         */
        sort(nums.begin(), nums.end());
        int moves = 0;
        for (int i = 1; i < nums.size(); ++i) {
            nums[i] += moves;
            moves += nums[i] - nums[i - 1];
        }
        return moves;
    }
};
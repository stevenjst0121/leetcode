#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        /**
         * [MEMO] Count length starting from num where num-1 not in nums
         */
        unordered_set<int> nums_set(nums.begin(), nums.end());
        int max_length = 0;
        for (auto num : nums) {
            if (nums_set.find(num - 1) != nums_set.end()) {
                continue;
            }

            int length = 1;
            int current_num = num + 1;
            while (nums_set.find(current_num) != nums_set.end()) {
                ++current_num;
                ++length;
            }
            max_length = max(max_length, length);
        }

        return max_length;
    }
};
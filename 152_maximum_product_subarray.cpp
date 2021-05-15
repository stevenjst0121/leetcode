#include <tuple>
#include <vector>

using namespace std;

class Solution {
 public:
  int maxProduct(vector<int>& nums) {
    /*Solution
    [MEMO] Only need to track previous max/min so far
    */
    size_t i = nums.size() - 1;
    int maxSoFar = nums.back();
    int minSoFar = nums.back();
    int maxMax = nums.back();

    for (size_t i = nums.size() - 2; i != (size_t)-1; --i) {
      int curr = nums[i];
      if (curr >= 0) {
        int tempMax = max(curr, curr * maxSoFar);
        minSoFar = min(curr, curr * minSoFar);
        maxSoFar = tempMax;
      } else {
        int tempMax = max(curr, curr * minSoFar);
        minSoFar = min(curr, curr * maxSoFar);
        maxSoFar = tempMax;
      }

      if (maxSoFar > maxMax) {
        maxMax = maxSoFar;
      }
    }

    return maxMax;
  }

 public:
  int maxProduct(vector<int>& nums) {
    /*Draft 1
    Got the DP idea right, but can be improved
    */
    size_t i = nums.size() - 1;
    vector<tuple<int, int>> dp(nums.size(), make_tuple(INT_MIN, INT_MAX));
    dp.back() = make_tuple(nums.back(), nums.back());
    int curr_max = INT_MIN;

    for (size_t i = nums.size() - 2; i != (size_t)-1; --i) {
      int _max, _min;
      if (nums[i] >= 0) {
        _max = nums[i] * get<0>(dp[i + 1]);
        _min = nums[i] * get<1>(dp[i + 1]);
      } else {
        _max = nums[i] * get<1>(dp[i + 1]);
        _min = nums[i] * get<0>(dp[i + 1]);
      }
      dp[i] = make_tuple(max(_max, nums[i]), min(_min, nums[i]));
    }

    const auto& result =
        max_element(dp.cbegin(), dp.cend(),
                    [](const tuple<int, int>& t1, const tuple<int, int>& t2) {
                      return get<0>(t1) < get<0>(t2);
                    });
    return get<0>(*result);
  }
};
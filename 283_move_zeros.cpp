#include <vector>

using namespace std;

class Solution {
 public:
  void moveZeroes(vector<int> &nums) {
    size_t firstZero = 0;
    while (firstZero < nums.size() && nums[firstZero] != 0) {
      ++firstZero;
    }
    if (firstZero == nums.size()) {
      // No zero in array
      return;
    }

    for (size_t i = firstZero + 1; i != nums.size(); ++i) {
      if (nums[i] != 0) {
        nums[firstZero] = nums[i];
        nums[i] = 0;
        ++firstZero;
      }
    }
    return;
  }
};
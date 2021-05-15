#include <vector>

using namespace std;

class Solution {
 public:
  int findDuplicate(vector<int> &nums) {
    /* Draft 2
    O(N) time O(1) space
    When sees a number, use the number as index and mark that value as -1
    (indicate the number is seen already)
    */
    size_t i = 0;
    while (i != nums.size()) {
      if (nums[i] < 0) {
        ++i;
        continue;
      }

      if (nums[nums[i] - 1] < 0) {
        return nums[i];
      }

      if (nums[i] - 1 == i) {
        int temp = nums[i];
        nums[i] = nums[nums[i] - 1];
        nums[temp - 1] = -1;
        ++i;
      } else {
        int temp = nums[i];
        nums[i] = nums[nums[i] - 1];
        nums[temp - 1] = -1;
      }
    }
    return -1;
  }
};
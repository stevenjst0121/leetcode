#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        /**
         * [MEMO]
         * Brilliant moving window solution
         */
        if (k <= 1) {
            return 0;
        }

        long prod = 1;
        int count = 0;
        int i = 0;
        for (int j = 0; j < nums.size(); ++j) {
            prod *= nums[j];
            while (prod >= k) {
                prod /= nums[i++];
            }
            count += j - i + 1;
        }
        return count;
    }

    int findLeastSumLogK(const vector<double>& logsums, int index, double logk) {
        int start = 0, end = index;
        while (start < end) {
            int mid = start + (end - start) / 2;
            double diff = logsums[index] - logsums[mid] - logk;
            if (diff > 0 || abs(diff) < 1e-14) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return start;
    }

    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        /**
         * [MEMO]
         * Use log() to replace product
         * But be careful when compaing equal doubles
         * When array is sorted, always think about using binary search
         */
        double logsum = 0.0;
        vector<double> logsums{0.0}; // add 0 for convenience
        for (auto num : nums) {
            logsum += log(num);
            logsums.push_back(logsum);
        }
        double logk = log(k);

        int count = 0;
        for (int i = 1; i <= nums.size(); ++i) {
            int start = findLeastSumLogK(logsums, i, logk);
            count += (i - start);
        }
        return count;
    }
};
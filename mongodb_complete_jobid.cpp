// https://www.1point3acres.com/bbs/thread-665240-1-1.html

#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    Solution() : d_maxJobId(INT_MIN) {}
    void complete(int jobId) {
        d_completedJobs.push_back(jobId);

        d_maxJobId = max(d_maxJobId, jobId);
    }
    int getLargestCompletedJobId() {
        if (d_completedJobs.empty()) {
            return -1;
        }

        return d_maxJobId;
    }

private:
    vector<int> d_completedJobs;
    int d_maxJobId;
};
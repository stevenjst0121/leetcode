#include <iostream>
#include <vector>

using namespace std;

int lowerbound(const vector<int>& list, int val) {
    int lo = 0, hi = list.size();
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (list[mid] < val) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return lo;
}

int upperbound(const vector<int>& list, int val) {
    int lo = 0, hi = list.size();
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (list[mid] <= val) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return lo;
}

int main(int argc, char** argv) {
    vector<int> list{1, 2, 3, 4, 4, 4, 4, 5};
    int i = upperbound(list, 4);
    cout << i << endl;
    int j = lowerbound(list, 4);
    cout << j << endl;
}
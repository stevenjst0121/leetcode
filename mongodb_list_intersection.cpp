// https://www.1point3acres.com/bbs/thread-665240-1-1.html

#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> list_intersection(vector<int>& list_1, vector<int>& list_2) {
        unordered_map<int, int> counter_1;
        for (auto val : list_1) {
            counter_1[val] += 1;
        }

        vector<int> result;
        for (auto val : list_2) {
            if (counter_1.find(val) != counter_1.end() && counter_1[val] > 0) {
                result.push_back(val);
                --counter_1[val];
            }
        }

        return result;
    }
};

template <typename T>
void print_vector(const vector<T>& v) {
    for (const auto& e : v) {
        cout << e << " ";
    }
    cout << endl;
}

int main(int argc, char** argv) {
    Solution s;
    vector<int> list_1{1, 1, 2, 2, 3, 3, 4, 5, 5, 6};
    vector<int> list_2{1, 2, 2, 2, 2, 4, 4, 6};
    auto result = s.list_intersection(list_1, list_2);
    print_vector(result);
}
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        /**
         * [MEMO] how the logic is simplified
         */
        if (numRows == 1) {
            return s;
        }

        vector<string> v(numRows, "");

        int row = 0;
        bool goingDown = false;
        for (auto c : s) {
            v[row] += c;
            if (row == 0 || row == numRows - 1) {
                goingDown = !goingDown;
            }
            row += goingDown ? 1 : -1;
        }

        string result;
        for (auto row : v) {
            result += row;
        }

        return result;
    }
};

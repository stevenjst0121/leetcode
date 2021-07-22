#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

class ScoreGreater {
public:
    bool operator()(const pair<string, int>& left, const pair<string, int>& right) {
        return left.second > right.second;
    }
};

class Solution {
public:
    Solution(int k) : d_k(k) {}
    void addScore(const string& name, int score) {
        d_scores.emplace_back(make_pair(name, score));

        d_topScores.push(make_pair(name, score));
        if (d_topScores.size() > d_k) {
            d_topScores.pop();
        }
    }
    vector<int> getTopKScores() {
        vector<int> result;
        while (!d_topScores.empty()) {
            result.push_back(d_topScores.top().second);
            d_topScores.pop();
        }
        return std::move(result);
    }

private:
    int d_k;
    vector<pair<string, int>> d_scores;
    priority_queue<pair<string, int>, vector<pair<string, int>>, ScoreGreater> d_topScores;
};

template <typename T>
void print_vector(const vector<T>& v) {
    for (const auto& e : v) {
        cout << e << " ";
    }
    cout << endl;
}

int main(int argc, char** argv) {
    Solution s(5);
    s.addScore("A", 50);
    s.addScore("B", 60);
    s.addScore("C", 70);
    s.addScore("D", 100);
    s.addScore("E", 100);
    s.addScore("F", 90);
    s.addScore("G", 20);

    auto result = s.getTopKScores();
    print_vector(result);
}
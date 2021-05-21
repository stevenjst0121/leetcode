/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    /**
     * Solution recursive
     * [MEMO] Was using the actual lower/upper value with INT_MIN/INT_MAX
     * Try to use nullptr (similar to None in python)
     */
    bool isValidBST(TreeNode* root) { return dfs(root, nullptr, nullptr); }
    bool dfs(TreeNode* node, TreeNode* lower, TreeNode* upper) {
        if (!node) {
            return true;
        }

        if (lower && node->val <= lower->val || upper && node->val >= upper->val) {
            return false;
        }

        return dfs(node->left, lower, node) && dfs(node->right, node, upper);
    }
};
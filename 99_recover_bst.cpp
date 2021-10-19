#include <vector>

using namespace std;

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
    void recoverTree(TreeNode* root) {
        // MEMO
        // The way to find two swapped values while traversing
        vector<TreeNode*> stack;
        TreeNode *x = nullptr, *y = nullptr, *prev = nullptr, *node = root;
        while (node || !stack.empty()) {
            if (node) {
                stack.push_back(node);
                node = node->left;
                continue;
            }

            node = stack.back();
            stack.pop_back();
            if (prev && node->val < prev->val) {
                y = node;
                if (!x) {
                    x = prev;
                } else {
                    break;
                }
            }

            prev = node;
            node = node->right;
        }

        swap(x->val, y->val);
    }
};

class Solution2 {
public:
    void recoverTree(TreeNode* root) {
        // MEMO
        // O(1) space with use of Morris Traversal
        TreeNode* x = nullptr;
        TreeNode* y = nullptr;
        TreeNode* predecessor = nullptr;
        TreeNode* pred = nullptr;
        TreeNode* node = root;

        while (node) {
            if (!node->left) {
                if (pred && node->val < pred->val) {
                    y = node;
                    if (!x) {
                        x = pred;
                    }
                }

                pred = node;
                node = node->right;
            } else {
                predecessor = node->left;
                while (predecessor->right && predecessor->right != node) {
                    // Be careful to stop when predecessor->right == node, which means we found a
                    // link
                    predecessor = predecessor->right;
                }

                if (!predecessor->right) {
                    // Form a link and continue to next node
                    predecessor->right = node;
                    node = node->left;
                } else {
                    // Current node has a link pointing to it, deal with the node
                    if (pred && node->val < pred->val) {
                        y = node;
                        if (!x) {
                            x = pred;
                        }
                    }

                    pred = node;
                    predecessor->right = nullptr;
                    node = node->right;
                }
            }
        }

        swap(x->val, y->val);
    }
};

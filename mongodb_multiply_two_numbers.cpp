#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    ListNode() = default;
    ListNode(int _val) : val(_val) {}
    int val;
    ListNode* next;
};

ostream& operator<<(ostream& os, ListNode* head) {
    if (!head) {
        return os;
    }

    os << head->next;
    os << head->val;
    return os;
}

class Solution {
public:
    ListNode* add_two_numbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode();
        ListNode* curr = head;
        int plus_one = 0;
        while (l1 || l2 || plus_one > 0) {
            int sum = 0;
            if (l1) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                sum += l2->val;
                l2 = l2->next;
            }
            sum += plus_one;
            plus_one = sum / 10;
            curr->next = new ListNode(sum % 10);
            curr = curr->next;
        }
        return head->next;
    }

    ListNode* multiply_number_and_digit(ListNode* l1, int digit) {
        // digit should be positive single digit
        cout << "multiply " << l1 << " and " << digit << endl;
        if (digit == 0) {
            return new ListNode(0);
        }

        ListNode* head = new ListNode();
        ListNode* curr = head;
        int plus = 0;
        while (l1 || plus > 0) {
            int product = 0;
            if (l1) {
                product = l1->val * digit;
                l1 = l1->next;
            }
            product += plus;
            plus = product / 10;
            curr->next = new ListNode(product % 10);
            curr = curr->next;
        }
        cout << head->next << endl;
        return head->next;
    }

    ListNode* append_zeros_to_num(ListNode* l1, int num_of_zeros) {
        ListNode* head = new ListNode();
        head->next = l1;
        for (int i = 0; i < num_of_zeros; ++i) {
            ListNode* next = head->next;
            head->next = new ListNode(0);
            head->next->next = next;
        }
        return head->next;
    }

    ListNode* multiply_two_numbers(ListNode* l1, ListNode* l2) {
        ListNode* result = new ListNode(0);
        int multiplier = 0;
        while (l1) {
            if (l1->val > 0) {
                ListNode* curr = multiply_number_and_digit(l2, l1->val);
                curr = append_zeros_to_num(curr, multiplier);
                result = add_two_numbers(result, curr);
            }
            ++multiplier;
            l1 = l1->next;
        }
        return result;
    }
};

int main(int argc, char** argv) {
    ListNode* l1 = new ListNode(9);
    l1->next = new ListNode(9);
    l1->next->next = new ListNode(5);

    ListNode* l2 = new ListNode(0);
    l2->next = new ListNode(0);
    l2->next->next = new ListNode(9);
    cout << l1 << endl;
    cout << l2 << endl;

    Solution s;
    // auto sum = s.add_two_numbers(l1, l2);
    // cout << sum << endl;

    auto product = s.multiply_two_numbers(l1, l2);
    cout << product << endl;
}

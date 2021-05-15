using namespace std;

// Definition for a Node.
class Node {
 public:
  int val;
  Node* next;

  Node() {}

  Node(int _val) {
    val = _val;
    next = nullptr;
  }

  Node(int _val, Node* _next) {
    val = _val;
    next = _next;
  }
};

class Solution {
 public:
  Node* insert(Node* head, int insertVal) {
    /*Two pointer solution
      Very similar to draft 1, but logic is bit more clear with two pointer
    */
    if (!head) {
      head = new Node(insertVal);
      head->next = head;
      return head;
    }

    Node* prev = head;
    Node* curr = head->next;
    Node* tail = nullptr;
    do {
      if (prev->val <= insertVal && curr->val >= insertVal) {
        prev->next = new Node(insertVal);
        prev->next->next = curr;
        return head;
      }

      if (prev->val > curr->val) {
        tail = prev;
      }

      prev = prev->next;
      curr = curr->next;
    } while (prev != head);

    if (tail) {
      Node* temp = tail->next;
      tail->next = new Node(insertVal);
      tail->next->next = temp;
    } else {
      prev->next = new Node(insertVal);
      prev->next->next = curr;
    }
    return head;
  }

 public:
  Node* insert(Node* head, int insertVal) {
    /*Draft 1
      O(N) and beats 74%
      Not super intuitive to cover all cases:
      1. insertVal is smallest -> insert after end
      2. insertVal is biggest -> insert after end
      3. insertVal is in between -> insert in middle
      * Also need to consider the situation where all nodes have the same value
      (flat)
    */
    if (!head) {
      head = new Node(insertVal);
      head->next = head;
      return head;
    }

    Node* node = head;
    Node* end = nullptr;
    do {
      if (node->val > node->next->val) {
        end = node;
      }
      if (node->val <= insertVal && node->next->val >= insertVal) {
        Node* temp = node->next;
        node->next = new Node(insertVal);
        node->next->next = temp;
        return head;
      }
      node = node->next;
    } while (node != head);

    if (end) {
      Node* temp = end->next;
      end->next = new Node(insertVal);
      end->next->next = temp;
    } else {
      Node* temp = head->next;
      head->next = new Node(insertVal);
      head->next->next = temp;
    }

    return head;
  }
};
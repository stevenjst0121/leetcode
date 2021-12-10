## Morris Inorder Traversal

There are three general ways to inorder traverse a BST in O(N) time complexity:
- Recursion: easiest to write, but may cause stack overflow
- Iterative: best time performance, but would need a stack that can use up to O(N) space
- Morris: uses only constant space

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        curr = root
        while curr:
            if curr.left is None:
                # Curr has no left child, yield curr and go to right
                result.append(curr.val)
                curr = curr.right
            else:
                # Find rightmost node of curr.left
                # while checking if there is a link pointing to curr
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                    
                if not pre.right:
                    # We found the right most node of curr.left
                    # Add link and continue
                    pre.right = curr
                    curr = curr.left
                else:
                    # We found a link to curr, which means we need to yield curr
                    # and break the link
                    pre.right = None
                    result.append(curr.val)
                    curr = curr.right

        return result
```

## Finding Two Swapped Values In Sorted

99. Recover BST
Use of two variables `x` and `y` to record bad values, assign to y first when found, and set x too if x was not assigned before

```python
if prev and curr.val < prev.val:
    y = curr
    if not x:
        x = prev
prev = curr
```

Because this is BST, so need to use prev to track previous node. If it's just a simple list, directly use \[i - 1\] and \[i\]

## Special Dynamic Programming

279. Perfect Squares

Try harder when thinking if the problem has optimal sub-problems. This one's subproblem is not so obvious to see.

```python
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [1]
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            if int(sqrt(i)) > sqrt(squares[-1]):
                squares.append(i)
            
            minimum = float("Inf")
            for square in squares:
                minimum = min(minimum, 1 + dp[i - square])
            dp[i] = minimum
            
        return dp[-1]
```

## Segment Tree

307. Range Sum Query

Segment tree can be implemented using either an array or a binary tree. 

```python
class NumArray:
    """
    [MEMO] Segment Tree recursive implementation
    """

    def __init__(self, nums: List[int]):
        # Array implementation
        self.N = len(nums)
        self.H = ceil(log2(self.N))
        self.tree = [0] * (2 * (2 ** self.H) - 1)
        self.buildTree(nums, 0, 0, self.N - 1)

    def buildTree(self, nums, tree_index, lo, hi):
        if lo == hi:
            self.tree[tree_index] = nums[lo]
            return

        mid = lo + (hi - lo) // 2
        self.buildTree(nums, 2 * tree_index + 1, lo, mid)
        self.buildTree(nums, 2 * tree_index + 2, mid + 1, hi)
        self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]

    def update(self, index: int, val: int) -> None:
        self.updateUtil(0, 0, self.N - 1, index, val)

    def updateUtil(self, tree_index: int, lo: int, hi: int, index: int, val: int) -> None:
        if lo == hi:
            self.tree[tree_index] = val
            return

        mid = lo + (hi - lo) // 2
        if index > mid:
            self.updateUtil(2 * tree_index + 2, mid + 1, hi, index, val)
        elif index <= mid:
            self.updateUtil(2 * tree_index + 1, lo, mid, index, val)

        self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeUtil(0, 0, self.N - 1, left, right)

    def sumRangeUtil(self, tree_index: int, lo: int, hi: int, left: int, right: int) -> int:
        if lo > right or hi < left:
            # Completely out of range
            return 0

        if left <= lo and right >= hi:
            # Completely in range
            return self.tree[tree_index]

        mid = lo + (hi - lo) // 2
        if left > mid:
            return self.sumRangeUtil(2 * tree_index + 2, mid + 1, hi, left, right)
        elif right <= mid:
            return self.sumRangeUtil(2 * tree_index + 1, lo, mid, left, right)

        left = self.sumRangeUtil(2 * tree_index + 1, lo, mid, left, mid)
        right = self.sumRangeUtil(2 * tree_index + 2, mid + 1, hi, mid + 1, right)

        return left + right
```

```python
class NumArray:
    class Node:
        def __init__(self, val: int = 0):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self, nums: List[int]):
        # Tree implementation
        self.N = len(nums)
        self.root = self.buildTree(nums, 0, self.N - 1)

    def buildTree(self, nums, lo, hi):
        if lo == hi:
            return NumArray.Node(nums[lo])

        mid = lo + (hi - lo) // 2
        left = self.buildTree(nums, lo, mid)
        right = self.buildTree(nums, mid + 1, hi)
        node = NumArray.Node(left.val + right.val)
        node.left = left
        node.right = right
        return node

    def update(self, index: int, val: int) -> None:
        self.updateTree(self.root, 0, self.N - 1, index, val)

    def updateTree(self, node, lo, hi, index, val):
        if lo == hi:
            node.val = val
            return

        mid = lo + (hi - lo) // 2
        if mid < index:
            self.updateTree(node.right, mid + 1, hi, index, val)
        else:
            self.updateTree(node.left, lo, mid, index, val)

        node.val = node.left.val + node.right.val

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeTree(self.root, 0, self.N - 1, left, right)

    def sumRangeTree(self, node, lo, hi, left, right):
        if hi < left or right < lo:
            return 0

        if left <= lo and hi <= right:
            return node.val

        mid = lo + (hi - lo) // 2
        if left > mid:
            return self.sumRangeTree(node.right, mid + 1, hi, left, right)
        elif right <= mid:
            return self.sumRangeTree(node.left, lo, mid, left, right)
        else:
            l = self.sumRangeTree(node.left, lo, mid, left, right)
            r = self.sumRangeTree(node.right, mid + 1, hi, left, right)
            return l + r
```

## Disjoint Set / Find Union

* Gist is to use a container to keep track of representatives of each group, starting with every node forms a group and the group's rep is itself
* Define `find` function to recursively find a node's rep
* Define `union` function to join two nodes, return True if join successful, False if they are already in the same group

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """Solution 2
        [MEMO] Use Disjoint Set/Union Find
        """
        reps = [i for i in range(n)]
        components = n
        for node1, node2 in edges:
            if self.union(reps, node1, node2):
                components -= 1
        return components

    def find(self, reps, node):
        if node == reps[node]:
            return node

        rep = self.find(reps, reps[node])
        reps[node] = rep
        return rep

    def union(self, reps, node1, node2):
        rep1 = self.find(reps, node1)
        rep2 = self.find(reps, node2)

        if rep1 == rep2:
            return False

        reps[rep2] = rep1
        return True
```

## Russian Doll Envelopes

* Sort envelopes increasingly by width but decreasingly by height, and then use stack to build an increasing height subsuence
```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -1 * x[1]))
        
        stack = []
        for _, h in envelopes:
            idx = bisect_left(stack, h)
            if idx == len(stack):
                stack.append(h)
            else:
                stack[idx] = h
        return len(stack)
```

## Distinct Subsequences II

```python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # [MEMO]
        # Trick is to count empty sequence during DP and minus it in the end
        # Trick is to keep track of dp result prev of adding a certain letter, which represents duplicate when that letter appears again
        dp = [1]
        last = {}
        for i, c in enumerate(s):
            dp.append(2 * dp[-1])
            if c in last:
                dp[-1] -= dp[last[c]]
            last[c] = i

        return (dp[-1] - 1) % (10 ** 9 + 7)
```

## Longest String Chain

* Smart DP using dictionary of words, dp[word] = max(dp[cut_word]) + 1
```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda word: len(word))
        dp = {}
        
        for word in words:
            if len(word) == 1:
                dp[word] = 1
                continue
            
            longest = 1
            for i in range(len(word)):
                cut_word = word[:i] + word[i + 1:]
                length = dp.get(cut_word, 0) + 1
                longest = max(longest, length)
            dp[word] = longest
        
        return max(dp.values())
```

## Number of Unique Good Subsequences

* Trick is still DP, but dp with counting number of good subsequences ending in 0 and 1 separately
```python
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        dp_0 = 0
        dp_1 = 0
        has_zero = 0
        for c in binary:
            val = int(c)
            if val == 0:
                dp_0 = dp_0 + dp_1
                has_zero = 1
            else:
                dp_1 = dp_0 + dp_1 + 1
        return (dp_0 + dp_1 + has_zero) % (10**9 + 7)
```

316. Remove Duplicate Letters

* Hard to come up with the strategy on how to get to the solution without brute-forcing.
```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # [MEMO]
        # Need to understand the problem, what's the strategy to pick one letter at a time
        c = Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            c[s[i]] -= 1
            if c[s[i]] == 0:
                break

        return s[pos] + self.removeDuplicateLetters(s[pos + 1 :].replace(s[pos], "")) if s else ""

    def removeDuplicateLetters(self, s: str) -> str:
        # [MEMO]
        # Brillliant usage of a stack, strategy is hard to think of
        stack = []
        seen = set()
        lasts = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and lasts[stack[-1]] > i:
                    seen.remove(stack.pop())
                stack.append(c)
                seen.add(c)
        return "".join(stack)
```

#### 5. Longest Palindromic Substring
<details>
<summary>See Memo</summary>

* dp[i][j]
* start building dp from the end
  
</details>

#### 18. 4Sum
<details>
<summary>See Memo</summary>

* sort array in order to remove duplicates
* Initial check
```python
if len(nums) < k or nums[0] * k > target or nums[-1] * k < target:
    return []
```

* Skip duplicates in while loop
```python
# twoSum
while lo < hi:
	...
	if sum < target or (lo > start and nums[lo - 1] == nums[lo]):
	...
	elif sum > target or (hi < len(nums) - 1 and nums[hi + 1] == nums[hi]):
	...
```

* Be careful with looping from start

</details>

#### 23. Merge k Sorted Lists
<details>
<summary>See Memo</summary>

* Use heapq (ListNode must be comparable, need to define __lt__ and __le__)
* Use divide and conquer
```python
interval = 1
while interval < k:
    for i in range(0, k - interval, interval * 2):
        lists[i] = self.merge2Lists(lists[i], lists[i + interval])
    interval *= 2
```

</details>

#### 31. Next Permutation
<details>
<summary>See Memo</summary>

* Starting from right, the first number that is smaller than its succeeding number is the one that needs to be changed
* Find the least bigger number from the right, swap them
* Reverse the rest

</details>

#### 41. First Missing Positive
<details>
<summary>See Memo</summary>

* Smallest possible missing positive is 1
* Solution must be in [1, N + 1], so mark all impossible values as 1
* Calculate corresponding index for each num and mark negative if it exists
```python
for i in range(len(nums)):
	index = abs(nums[i]) - 1
	if index < len(nums) and nums[index] > 0:
		nums[index] = -nums[index]
```
* Loop through and find first positive, its index is the first missing positive

</details>

#### 42. Trapping Rain Water
<details>
<summary>See Memo</summary>

* Basic idea is at each location, the trapped water is min(max_left, max_right) - height
* Calculate max_left and max_right separately and then calculate trapped water
* There is also two pointer solution which saves 1 iteration

</details>

#### 46. Permutations
<details>
<summary>See Memo</summary>

* Backtrack - an algorithm for finding all solutions by exploring all potential candidates
* Stop condition
* Remember to do `nums.copy()`
```python
def backtrack(self, nums: List[int], start: int) -> None:
	if start == len(nums):
		self.result.append(nums.copy())
	
	for i in range(start, len(nums)):
		nums[start], nums[i] = nums[i], nums[start]
		self.backtrack(nums, start + 1)
		nums[start], nums[i] = nums[i], nums[start]
```

</details>

#### 47. Permutations II
<details>
<summary>See Memo</summary>

* The difference between 47 and 46 is duplicates, the backtrack solution in 46 would not be able to avoid duplicates
* Instead of rearranging backtrack like 46, use counter to build combination up
* This solution would apply to both 46 and 47
```python
def backtrack(self, comb: List[int], N: int, counter: Dict) -> None:
	if len(comb) == N:
		self.result.append(comb.copy())
		return
	
	for num in counter:
		if counter[num] > 0:
			counter[num] -= 1
			comb.append(num)
			self.backtrack(comb, N, counter)
			comb.pop()
			counter[num] += 1
```

</details>

#### 48. Rotate Image
<details>
<summary>See Memo</summary>

* The way to loop is tricky
* To figure out which location gets where, just write down some samples, e.g. (0, 0) -> (0, 2), (0, 1) -> (1, 2)...
```python
N = len(matrix)
for i in range(N // 2 + N % 2):
	for j in range(N // 2):
		tmp = matrix[i][j]
		matrix[i][j] = matrix[N - j - 1][i]
		matrix[N - j - 1][i] = matrix[N - i - 1][N - j - 1]
		matrix[N - i - 1][N - j - 1] = matrix[j][N - i - 1]
		matrix[j][N - i - 1] = tmp
```

</details>

#### 56. Merge Intervals
<details>
<summary>See Memo</summary>

* Sort the intervals (use lambda)
* Use stack and always merge with the last interval in stack

</details>

#### 76. Minimum Window Substring
<details>
<summary>See Memo</summary>

* Not suitable for DP
* Moving window idea
	* Two pointers lo and hi
	* Use hi to expand the upper range of moving window
	* Use lo to contract the lower range of moving window
	* During loop, use counter to check if a certain character has met required number
	* Instead of comparing counter directly, use a formed tracker to track the number of formed characters

</details>

#### 84. Largest Rectangle in Histogram
<details>
<summary>See Memo</summary>

**Stack O(N)**
* Keep all bars in stack in ascending order
* Whenever see a bar that is smaller than the last bar in stack, calculate previous areas until the bar that is smaller than current bar
* Use -1 to mark the one before begining position for calculating width
```python
stack = [-1]
max_area = 0
for i in range(len(heights)):
	while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
		current_height = heights[stack.pop()]
		current_width = i - stack[-1] - 1
		max_area = max(max_area, current_height * current_width)
	stack.append(i)

while stack[-1] != -1:
	current_height = heights[stack.pop()]
	current_width = len(heights) - stack[-1] - 1
	max_area = max(max_area, current_height * current_width)
return max_area
```

**Divide and Conquer O(NLogN)**
```python
if not heights:
	return 0

min_index = 0
for i in range(len(heights)):
	if heights[i] < heights[min_index]:
		min_index = i
return max(
	heights[min_index] * len(heights),
	self.largestRectangleArea(heights[:min_index]),
	self.largestRectangleArea(heights[min_index + 1 :]),
)
```

</details>

#### 85. Maximal Rectangle
<details>
<summary>See Memo</summary>

**DP Solution**
* Calculate maximum width of every row end at every dp[i][j]
* For every dp[i][j] > 0, move up the cursor and update max_area
```python
max_area = 0

dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
for i in range(len(matrix)):
	for j in range(len(matrix[0])):
		if matrix[i][j] == "0":
			continue

		if j > 0:
			width = dp[i][j - 1] + 1
		else:
			width = 1
		dp[i][j] = width

		for k in range(i, -1, -1):
			width = min(width, dp[k][j])
			max_area = max(max_area, width * (i - k + 1))
return max_area
```

**Stack Solution**
* Calculate maximum width of every row end at every dp[i][j]
* For each column, we have a histogram of heights.
* Use same stack solution as in 84 to calculate max rectangle in histograms for each column.

</details>

#### 91. Decode Ways
<details>
<summary>See Memo</summary>

* DP bottom-up, build from right side
* Because this DP needs to know two previous states, dp[i + 1] and dp[i + 2], trick here is to create DP of size `N + 1`

</details>

#### 99. Recover Binary Search Tree
<details>
<summary>See Memo</summary>

* How to find two swapped values in a almost sorted list
```c++
// Naive
int i = 0;
for (; i < list.size() - 1; ++i) {
	if (list[i]->val > list[i + 1]->val) {
		break;
	}
}
int j = list.size() - 1;
for (; j > i; --j) {
	if (list[j]->val < list[j - 1]->val) {
		break;
	}
}

swap(list[i]->val, list[j]->val);

// Better
if (prev && node->val < prev->val) {
	y = node;
	if (!x) {
		x = prev;
	} else {
		break;
	}
}
```
* Use of Morris algorithm to solve in O(1) space

</details>

#### 115. Distinct Subsequences
<details>
<summary>See Memo</summary>

\[Important\]

* Realize how an recursive approach looks like. Try to always think of using indexes with subsequences.
	- Recursive approach can be optimized using memoization, but still could cause call stack to overflow, and also with a lot of function call overhead.
* Bottom-up DP
	- `dp[i][j]` represents the unique number of subsequences of `s[i:]` for `t[j:]`
	- Use +1 array, e.g. M+1 * N+1
	- Be careful with the base cases
```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        
        for i in range(M + 1):
            dp[i][N] = 1
        
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j] + dp[i + 1][j + 1]
                else:
                    dp[i][j] = dp[i + 1][j]
        
        return dp[0][0]
```
* Think about whether a 2D array dp solution can be optimized on space to only use 1D array
```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        dp = [0] * (N + 1)
        
        for i in range(M - 1, -1, -1):
            prev = 1
            for j in range(N - 1, -1, -1):
                old = dp[j]
                if s[i] == t[j]:
                    dp[j] += prev
                prev = old
        
        return dp[0]
```
* See also 940 Distinct Subsequences II

</details>

#### 123. Best Time to Buy and Sell Stock III
<details>
<summary>See Memo</summary>

* Find max_proft_so_far from two sides
	- max profit from left till i
	- max profit from right till j
	- Find i == j where total profit is max

</details>

#### 127. Word Ladder

<details>
<summary>See Memo</summary>

* Build a graph from trans to set(words)
* Step-by-step BFS
* Bi-directional search
* One trick is to store the steps to get to each node along in `queue` and `visited`
```python
# Queue for iterating
queue_front = deque([(beginWord, 1)])
queue_back = deque([(endWord, 1)])

# Visited
visited_front = {beginWord: 1}
visited_back = {endWord: 1}

while queue_front and queue_back:
	steps = self.visitWordNode(queue_front, visited_front, visited_back)
	if steps > 0:
		return steps

	steps = self.visitWordNode(queue_back, visited_back, visited_front)
	if steps > 0:
		return steps

return 0
```

</details>

#### 133. Clone Graph
<details>
<summary>See Memo</summary>

* Recursive call to cloneNode and return created node directly
* Use a separate map to track newly created nodes (no need to use visited any more)

</details>

#### 136. Single Number
<details>
<summary>See Memo</summary>

* Bit manipulation XOR
	* 0 ^ a = a
	* a ^ a = 0
	* a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b

</details>

#### 138. Copy List with Random Pointer
<details>
<summary>See Memo</summary>

* All immutable objects are hashable in python by default and all user defined class that contain only hashable objects are hashable by default
* Created an `added` map from old node to new node
* This problem can be solved both recursively or iteratively

</details>

#### 143. Reorder List
<details>
<summary>See Memo</summary>

* Use slow/fast pointer to find second half of list
```python
dummy_head = ListNode()
dummy_head.next = head
slow, fast = dummy_head, dummy_head
while fast and fast.next:
	slow = slow.next
	fast = fast.next.next

head_2 = slow.next
```
* Define `reverseList` to reverse a list (be careful 3) must happen before 4))
```python
def reverseList(self, head: ListNode) -> ListNode:
	if not head:
		return None
	
	newhead = ListNode()
	node = head
	while node:
		tmp = newhead.next
		newhead.next = node
		node = node.next # 3
		newhead.next.next = tmp # 4
	return newhead.next
```
* Define `mergeSecondList`. For this problem, cannot return new head. So make sure to merge second head into the first head directly.
```python
def mergeSecondList(self, head_1: ListNode, head_2: ListNode) -> None:
	curr_1 = head_1
	curr_2 = head_2
	while curr_2:
		temp = curr_1.next
		curr_1.next = curr_2
		curr_2 = curr_2.next
		curr_1.next.next = temp
		curr_1 = temp
```

</details>

#### 146. LRU Cache
<details>
<summary>See Memo</summary>

* Requires O(1) in getting value by key
* Requires O(1) in putting new key
* Requires O(1) in popping out the least recently used key
* Sorted key + hashmap

**OrderedDict**
* Use move_to_end(key) to move a recently used key to end (new keys are added to the end by default)
* Use popitem(False) to pop least recently used key from the top

**Dictionary + Doubly linked list**
* Define Node
```python
class Node:
	def __init__(self, key: int, val: int):
		self.key = key
		self.val = val
		self.prev = None
		self.next = None
```
* Define double linked list
```python
self.head = LRUCache.Node(0, 0)
self.tail = LRUCache.Node(0, 0)

self.head.next = self.tail
self.tail.prev = self.head
```
* Define `add_node`, `remove_node` and `move_node_to_head`
	* `add_node`: Add new node to head, need to worry about four edges. Always start with edges coming out of the new node:
	```python
	def add_node(self, node):
		"""
		Always add the new node right after head.
		"""
		node.prev = self.head
		node.next = self.head.next

		# [MEMO] This must run first!
		self.head.next.prev = node
		self.head.next = node
	```
	* `remove_node`: Remove node from list, need to worry about two edges coming in to the node
	```python
	def remove_node(self, node):
		node.prev.next = node.next
		node.next.prev = node.prev
	```
	* `move_node_to_head`: Use add and remove directly
	```python
	def move_node_to_head(self, node):
		self.remove_node(node)
		self.add_node(node)
	```

</details>

#### 152. Maximum Product Subarray
<details>
<summary>See Memo</summary>

* Need to track both `max_so_far` and `min_so_far` because product can change the sign
* Be careful to use `new_max_so_far` and `new_min_so_far` when updating
```python
def maxProduct(self, nums: List[int]) -> int:
	min_so_far = nums[-1]
	max_so_far = nums[-1]
	max_all = max_so_far
	
	for i in range(len(nums) - 2, -1, -1):
		new_max_so_far = max(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)
		new_min_so_far = min(nums[i], nums[i] * max_so_far, nums[i] * min_so_far)
		max_all = max(max_all, new_max_so_far)
		max_so_far = new_max_so_far
		min_so_far = new_min_so_far
	return max_all
```

</details>

#### 155. Min Stack
<details>
<summary>See Memo</summary>

**Value and min value pair**
* Store value along with min value so far in stack

**Two stacks**
* One stack to store the values
* Another stack to store the min values
```python
def push(self, val: int) -> None:
	self.stack.append(val)
	# THIS MUST BE <=
	if not self.min_tracker or val <= self.min_tracker[-1]:
		self.min_tracker.append(val)

def pop(self) -> None:
	if not self.stack:
		return

	val = self.stack.pop()
	if val == self.min_tracker[-1]:
		self.min_tracker.pop()
```

</details>

#### 204. Count Primes
<details>
<summary>See Memo</summary>

* DP, starting from smallest known prime, and cross off mutipliers of the number
* Trick 1: Only need to go to sqrt(N), larger nums will be crossed off
* Trick 2: When crossing off, stack from `i * i`
```python
def countPrimes(self, n: int) -> int:
	if n < 2:
		return 0
	
	dp = [1] * n
	dp[0] = 0
	dp[1] = 0
	i = 0
	while i < math.sqrt(n):
		if dp[i] == 0:
			i += 1
			continue
		
		for j in range(i * i, n, i):
			dp[j] = 0
		i += 1
	return sum(dp)
```

</details>

#### 207. Course Schedule
<details>
<summary>See Memo</summary>

**DFS**
* Use special visited tracking:
	1. In traverse
    2. Done traverse (node has no child or all children are visited)
* In DFS, when a node is in visited = 1, means there is cycle. 2 means done already.
```python
def hasCycle(self, course, graph, visited):
	if course in visited:
		if visited[course] == 1:
			return True
		elif visited[course] == 2:
			return False

	visited[course] = 1
	for neighbor in graph[course]:
		if self.hasCycle(neighbor, graph, visited):
			return True

	visited[course] = 2
```

**Topological Sort**
* Init `degrees` while building graph, degrees[course] means the number of prerequisites needed to take the course
* Use queue to take courses with 0 degrees first
* While taking courses, keep track of other courses and see if their prerequisites are taken
```python
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
	graph = defaultdict(set)
	degrees = [0] * numCourses

	for first, second in prerequisites:
		if first not in graph[second]:
			graph[second].add(first)
			degrees[first] += 1

	output = []
	queue = deque([course for course, num_deps in enumerate(degrees) if num_deps == 0])
	while queue:
		course = queue.pop()
		output.append(course)
		for neighbor in graph[course]:
			degrees[neighbor] -= 1
			if degrees[neighbor] == 0:
				queue.appendleft(neighbor)

	if len(output) < numCourses:
		return []
	return output
```

</details>

#### 210. Course Schedule II
<details>
<summary>See Memo</summary>

* Very similar to 207 above
* Both methods in 207 can be used
	* DFS - Add node to output when marking a node as visited = 2
	* Topological sort - output courses with 0 degrees first

</details>

#### 211. Design Add and Search Words Data Structure
<details>
<summary>See Memo</summary>

* Trie, can just be implemented as a simple dictionary
* End-of-word can use some special character, e.g. `$`
* If search have wildcard, define `search_in_node`. During search be careful in handing `$` when searching `.`
* `return "$" in node`

</details>

#### 215. Kth Largest Element in an Array
<details>
<summary>See Memo</summary>

**Heap**

**Quick Select**
* A well-known algo to find kth smallest element in O(N), worst O(N^2)
	* Find pivot (use randint)
	* Move pivot to the end temporarily
	* Keep a pointer i that points to the smalles index larger than pivot
	* Loop through nums, when ever find a num smaller than nums[i], swap them and increment i
	* If i + 1 == ks, found solution. Otherwise recursive call
	```python
	def quickSelect(self, nums, low, high, ks):
        # find kth smallest
        # [NOTE] randint, low <= N <= high
        pivot_index = random.randint(low, high)
        pivot = nums[pivot_index]
        # move pivot to end
        nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
        i = low  # the lowest indices where num > pivot
        for j in range(low, high + 1):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]

        # i is pivot now
        if i == ks - 1:
            return nums[i]
        elif i > ks - 1:
            return self.quickSelect(nums, low, i - 1, ks)
        else:
            return self.quickSelect(nums, i + 1, high, ks)
	```

</details>

#### 221. Maximal Square
<details>
<summary>See Memo</summary>

* dp[i][j] represents the largest square length using (i, j) as bottom right square corner
* `dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1`

</details>

#### 227. Basic Calculator II
<details>
<summary>See Memo</summary>

* Use stack to track previous number and previous operation
* Start prev_op = "+"
* Remember the condition checks in order to handle end-of-string situration (It is possible that the last character is a number and you need to both calculate the number and take the previous operation)
* It is possible to not use stack though, just the last number in stack is good enough
```python
if c.isdigit():
    num = num * 10 + int(c)

if not c.isdigit() and c != " " or i == len(s) - 1:
	...
```

</details>

#### 236. Lowest Common Ancestor of a Binary Tree
<details>
<summary>See Memo</summary>

* DFS, return value to tell whether current path contains p or q

</details>

#### 253. Meeting Rooms II
<details>
<summary>See Memo</summary>

* Meeting start/end don't have to match exact meetings, only need to count how many meetings started and ended

</details>

#### 261. Graph Valid Tree
<details>
<summary>See Memo</summary>

**Solution 1**
* A graph is a tree if
	* There is no cycle
	* All nodes are connected

**Solution 2**
* A graph is a tree if
	* There are n - 1 edges
	* And all nodes are connecected
	* Above two implicits there is no cycle

</details>

#### 269. Alien Dictionary
<details>
<summary>See Memo</summary>

* Initialize degrees, have to do O(N^2) loop: `degrees = Counter{c: 0 for word in words for c in word}`
* Form graph and update degrees. Be care when two words have exact same front part, but first word is longer than second word.
* Topological sort to find possible result
* Result is only valid if it contains all the letters

</details>

#### 279. Perfect Squares
<details>
<summary>See Memo</summary>

* Should think of dp
```C++
class Solution {
public:
    int numSquares(int n) {
        // DP, O(n * sqrt(n))
        vector<int> squares = {1};
        int dp[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i <= n; ++i) {
            // Add perfect squares if needed
            if (static_cast<int>(sqrt(i)) > static_cast<int>(sqrt(squares.back()))) {
                squares.push_back(i);
            }

            // Find min
            int minnum = INT_MAX;
            for (auto square : squares) {
                if (i - square < 0) {
                    break;
                }

                minnum = min(minnum, 1 + dp[i - square]);
            }
            dp[i] = minnum;
        }

        return dp[n];
    }
};
```
* Should also think of Greedy approach, and here need to be greedy with the count of numbers
* Greedy approach can be further improved to a BFS of an N-ary tree
```C++
class Solution {
public:
    int numSquares(int n) {
        // [MEMO] BFS + N-ary tree
        // The above greedy solution is basically a BFS on an N-array tree,
        // where N is sqrt(N) - the number of perfect squares
        for (int i = 1; i <= sqrt(n); ++i) {
            d_squares.insert(i * i);
        }

        deque<int> queue = {n};
        int level = 1;
        while (level <= n) {
            int size = queue.size();
            for (int i = 0; i < size; ++i) {
                int res = queue.front();
                queue.pop_front();
                if (d_squares.find(res) != d_squares.end()) {
                    return level;
                }

                // Not found, form next level leaves
                for (auto square : d_squares) {
                    if (res - square > 0) {
                        queue.push_back(res - square);
                    }
                }
            }
            ++level;
        }

        return level;
    }

private:
    set<int> d_squares;
};
```

</details>

#### 297. Serialize and Deserialize Binary Tree
<details>
<summary>See Memo</summary>

* Follow DFS traverse (root, left and right)

</details>

#### 307. Range Sum Query - Mutable
<details>
<summary>See Memo</summary>

* Segment Tree implementation, helps to solve range-based questions
* Query and update are both O(LogN)

</details>

#### 311. Sparse Matrix Multiplication
<details>
<summary>See Memo</summary>

* For matrix 1, store non-zero positions by row da[m] = list(k)
* For matrix 2, store non-zero positions by col, db[n] = list[k]

</details>

#### 314. Binary Tree Vertical Order Traversal
<details>
<summary>See Memo</summary>

* BFS, put (row, col, node) into queue for traversal
* Store values of BFS by col in dict
* When output, traverse by `sorted(d.keys())`

</details>

#### 316. Remove Duplicate Letters
<details>
<summary>See Memo</summary>

* The important thing here is to understand the question, and come up with a strategy to find the result in O(N)
	* Letter by letter, choose one letter that has trailing letters contains all others. And choose the smallest letter if same
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
```

	* Using a stack to remove letters while building. Theory is that when we encounter a letter that is not seen before, remove all previous letters in stack that are larger than the current letter and has the same letter later at some point.

</details>
#### 322. Coin Change
<details>
<summary>See Memo</summary>

* Simple backtracking is basically brute force, will time out (maybe adding greedy would help?)
* Bottom-up dp on each amount level.
* Trick: in python, Int + 1 is still Inf
* coins sequence does not matter, simply because using which coin first for a coin change doesn't matter
```python
def coinChange(self, coins: List[int], amount: int) -> int:
	counts = [float("Inf")] * (amount + 1)
	counts[0] = 0
	for coin in coins:
		for x in range(coin, amount + 1):
			counts[x] = min(counts[x], counts[x - coin] + 1)
	return counts[-1] if counts[-1] != float("Inf") else -1
```

* This is a more intuitive DP, but a bit slower than solution above
* Basically for the sample data set, dp\[11\] = min(1 + dp\[10\], 1 + dp\[9\], 1 + dp\[6\])
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            num = float("Inf")
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] >= 0:
                    num = min(num, 1 + dp[i - coin])
            dp[i] = num if num < float("Inf") else -1
        
        return dp[-1]
```

* If bottom-up is hard to think of, use top-down (recursion + memoization), the key idea is to realize the optimal subproblem property.

</details>

#### 323. Number of Connected Components in an Undirected Graph
<details>
<summary>See Memo</summary>

* Define a dictionary for representative mapping (starting with using self as representative)
* [Option] Define size or other useful information
* Define `find` that is used to recursively find the current representative of a node
* Define `union` that combine two nodes into the same group
	* Check if their reps are the same
	* If yes, they are already in the same group
	* If not, merge them (set one rep to the other rep's rep)
* Start total number of components with n and call `union` on all edges, upon successful union, decrement component count

</details>

#### 332. Reconstruct Itinerary
<details>
<summary>See Memo</summary>

* Backtrack + Greedy
* Need some way to indicate if a ticket has been used, use defaultdict(list[[destination, True/False]])
* Backtrack needs to return True/False to indicate if the local optimal solution has reached a global optimal solutio`n

</details>

#### 341. Flatten Nested List Iterator
<details>
<summary>See Memo</summary>

* Basic idea is to use a stack for getting the next element
* Trick: Use reversed() function in order to use a normal stack

</details>

#### 354. [MEMO] Russian Doll Envelopes
<details>
<summary>See Memo</summary>

* Intuitively, backtrack can be applied, but time limit exceeded
* But it is really "Longest Increasing Subsequence" problem
```python
def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
	"""
	dp[i] represents LIS ending in i
	dp[i] = max(dp[j]) for each 0 <= j < i
	"""
	envelopes.sort(key=lambda x: (x[0], -1 * x[1]))

	max_russian = 0
	dp = [0] * len(envelopes)
	for i in range(len(envelopes)):
		max_j = 0
		for j in range(i):
			if envelopes[j][1] < envelopes[i][1]:
				max_j = max(max_j, dp[j])

		dp[i] = max_j + 1
		max_russian = max(max_russian, dp[i])
	return max_russian
```

* Longest Common Subsequence does not apply here, because pairs cannot be sorted in uniquely increasing way without removing some pairs.

</details>

#### 370. Range Addition
<details>
<summary>See Memo</summary>

* Could sort the updates by starting index, but still won't reduce time complexity much if all updates cover large ranges
* Cumulative sum!!! But only track increments at borders and read it out once. Time complexity is O(N) or O(M), whichever is larger.

</details>

#### 394. Decode String
<details>
<summary>See Memo</summary>

* Use stack to store everything
* When sees "]", trace back to find substring till "["

</details>

#### 399. Evaluate Division
<details>
<summary>See Memo</summary>

* Build graph a -> b and b -> a, result is basically path from a -> c
* Define dfs that returns value of node -> target, recursive call

</details>

#### 442. Find All Duplicates in an Array
<details>
<summary>See Memo</summary>

* Iterate and mark num index as negative
* Output result when see an num index is already marked negative

</details>

#### 523. Continuous Subarray Sum
<details>
<summary>See Memo</summary>

* Use dict to record the earlises location of mod = sum % k
* While traversing, calculate mod and see if the previous mod location is less than i - 1
* Trick: add sums[0] = -1

</details>

#### 528. Random Pick with Weight
<details>
<summary>See Memo</summary>

* Accumulative sum
* `random.random()` gets random number in [0.0, 1.0)
* Easiest way to write binary search
```python
def pickIndex(self) -> int:
	target = self.total * random.random()
	# run a binary search to find the target zone
	"""[MEMO+1] Easiest way to write binary search without recursion"""
	low, high = 0, len(self.w_accumulate) - 1
	while low < high:
		mid = (low + high) // 2
		if target > self.w_accumulate[mid]:
			low = mid + 1
		else:
			high = mid
	return low
```
</details>

#### 532. K-diff Pairs in an Array
<details>
<summary>See Memo</summary>

**set**
* Track seen nums in set and store result in set (O(1) to check duplicates)

**counter**
* Get counter of all numbers
* Loop through counter
	* Make sure to handle different cases for k > 0 and k == 0

</details>

#### 560. Subarray Sum Equals K
<details>
<summary>See Memo</summary>

* Use accumulative sum
* Trick, accu_sum[0] = 1 # empty

</details>

#### 670. Maximum Swap
<details>
<summary>See Memo</summary>

* Get last index for each num, loop through and find the most signifant index that can get a swap for a larger number
* Trick: use `list(str(num))`
* Trick: `last = {int(n): i for i, n in enumerate(nums)}`

</details>

#### 718. Maximum Length of Repeated Subarray
<details>
<summary>See Memo</summary>

* Use DP, where dp[i][j] represents the longest subarray starting from i in nums1 and j in nums2
* Trick: both dp size + 1
```python
def findLength(self, nums1: List[int], nums2: List[int]) -> int:
	dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
	for i in range(len(nums1) - 1, -1, -1):
		for j in range(len(nums2) - 1, -1, -1):
			if nums1[i] == nums2[j]:
				dp[i][j] = dp[i + 1][j + 1] + 1
	return max([max(length) for length in dp])
```

</details>

#### 721. Accounts Merge
<details>
<summary>See Memo</summary>

* Form undirected graph on emails based on input account (can just link all emails to the first email in account)
* Form a map that maps an email to the account name, for output
* Traverse through the graph and find all emails that are linked together and add to output

</details>

#### 740. Delete and Earn
<details>
<summary>See Memo</summary>

* Can probably do backtrack, but will cost a lot of time complexity
* Realize two facts:
	1. If you choose to delete a num, you are best just delete all of this num. This should make you think of using a Counter
	2. When you are given a num, you only have two choices - delete or keep. If we sort all nums in counter and start from the smallest, we need to keep track of two local results - delete or keep. Then we can build DP on top of this. (Similar to 152. Maximum Product Subarray)
* DP + sorted(Counter)
```python
def deleteAndEarn(self, nums: List[int]) -> int:
	count = Counter(nums)
	prev = None
	avoid, using = 0, 0
	for k in sorted(count):
		new_avoid = max(avoid, using)
		if k - 1 == prev:
			new_using = k * count[k] + avoid
		else:
			new_using = k * count[k] + max(avoid, using)
		prev = k
		avoid = new_avoid
		using = new_using
	return max(avoid, using)
```

</details>

#### 767. Reorganize String
<details>
<summary>See Memo</summary>

* Use max heap to pop out the two most counted char and put them together
* Trick: The operation is not possible if a number is too many:
	* If s has odd number characters, num > (N + 1) / 2
	* If s has even number characters, num > N // 2
	* So combine them, can just do (N + 1) / 2

</details>

#### 785. Is Graph Bipartite?
<details>
<summary>See Memo</summary>

* Use special visited map to value, if two linked nodes have the same value then it's not bipartite

</details>

#### 843. Guess the Word
<details>
<summary>See Memo</summary>

* Keep reducing wordlist while trying
* DO NOT create a map up-front

</details>

#### 895. Maximum Frequency Stack
<details>
<summary>See Memo</summary>

* The problem is tricky because you need some data structure that can tell the most frequent and latest push at the same time
* Initialize a stack per frequency, and keep track of the max frequency over time
```python
class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        self.max_freq = max(self.max_freq, self.freq[val])

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val
```

</details>

#### 912. Sort an Array
<details>
<summary>See Memo</summary>

* Quicksort
	* Partition (use high?)
	* quicksort left
	* quicksort right

* Mergesort
	* Partition (calculate mid)
	* mergesort left
	* mergesort right
	* merge left and right

</details>

#### 940. Distinct Subsequences II
<details>
<summary>See Memo</summary>

* Trick is to count empty sequence during DP and minus it in the end
* Trick is to keep track of dp result prev of adding a certain letter, which represents duplicate when that letter appears again

</details>

#### 986. Interval List Intersections
<details>
<summary>See Memo</summary>

* To check if two intervals have intersection:
```python
lo = max(firstList[i][0], secondList[j][0])
hi = min(firstList[i][1], secondList[j][1])
if lo <= hi:
	result.append([lo, hi])
```
* Two pointer, keep the larger interval and move the smaller

</details>

#### 987. Vertical Order Traversal of a Binary Tree
<details>
<summary>See Memo</summary>

* Traverse will tracking position
* Store (row, col, val) and record map by col, can directly sort on tuple

</details>

#### 1048. Longest String Chain
<details>
<summary>See Memo</summary>

* Sort words by len
* Bottom-up dp

</details>

#### 1143. Longest Common Subsequence
<details>
<summary>See Memo</summary>

```c++
vector<vector<int>> dp;
int n = text1.length(), m = text2.length();
for (int i = 0; i < n; ++i) {
	dp.emplace_back(m, 0);
}

for (int i = n - 1; i >= 0; --i) {
	for (int j = m - 1; j >= 0; --j) {
		if (text1[i] == text2[j]) {
			if (i == n - 1 || j == m - 1) {
				dp[i][j] = 1;
			} else {
				dp[i][j] = dp[i + 1][j + 1] + 1;
			}
		} else {
			if (i != n - 1 && j != m - 1) {
				dp[i][j] = max(dp[i][j + 1], dp[i + 1][j]);
			} else if (i != n - 1) {
				dp[i][j] = dp[i + 1][j];
			} else if (j != m - 1) {
				dp[i][j] = dp[i][j + 1];
			}
		}
	}
}
return dp[0][0];
```

</details>

#### 1153. String Transforms Into Another String
<details>
<summary>See Memo</summary>

* Realize the fact that each char only allow to be changed to another char
* Simply use a dictionary to mark such link and return False if one char needs to be converted to multiple chars

</details>

#### 1197. Minimum Knight Moves
<details>
<summary>See Memo</summary>

* Bi-directional BFS search
* Trick: Keep track of steps used (either directly in outer loop when calling bfs, or store steps in visited as a map)

</details>

#### 1209. Remove All Adjacent Duplicates in String II
<details>
<summary>See Memo</summary>

* Trick is similar to Min Stack, where you store some "so far" value along with the value in/side-by-side with stack
* Here we store counts of adjacent occurances of the last num in stack

</details>

#### 1249. Minimum Remove to Make Valid Parentheses
<details>
<summary>See Memo</summary>

* Basic idea is to traverse and add all invalid ")"s to to_remove set
* And then remove invalid "("s as well
* Trick: A brilliant solution is to keep track of opens = [], and pop from it if a valid ")" is found after. And the end, union to_remove and opens left

</details>

#### 1593. Split a String Into the Max Number of Unique Substrings
<details>
<summary>See Memo</summary>

* Cannot use DP as one bigger problem does not depends directly on its subproblems
	* Even use dp[i] = [count, set(substr)], there is no way to remember all possible unique sets
* Use backtrack

</details>

#### 1987. Number of Unique Good Subsequences
<details>
<summary>See Memo</summary>

* All good subsequences must start with '1', except for '0'.
* Trick is to count good subsequences ends in 0 and 1 separately
* '0' needs to considered separately as well

```c++
class Solution {
public:
    int numberOfUniqueGoodSubsequences(string binary) {
        // [MEMO] Brilliant DP solution
        // Trick is to count good subsequences ends in 0 and 1 separately
        // '0' needs to be counted separately
        int mod = 1e9 + 7, dp[2] = {0, 0};
        bool has_zero = false;
        for (auto& c : binary) {
            if (c == '0') {
                dp[0] = dp[0] + dp[1];
                has_zero = true;
            } else if (c == '1') {
                dp[1] = dp[0] + dp[1] + 1;
            }
        }
        
        return (dp[0] + dp[1] + has_zero) % mod;
    }
};
```

</details>

#### Template
<details>
<summary>See Memo</summary>

</details>

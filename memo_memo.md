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

#### 53. Maximum Subarray
<details>
<summary>See Memo</summary>

* dp bottom up
* Key concept is to determine if the current subarray is worth keeping or no (can start from begin or end)

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

#### 98. Validate Binary Search Tree
<details>
<summary>See Memo</summary>

* DFS with lower and upper range

</details>

#### 123. Best Time to Buy and Sell Stock III
<details>
<summary>See Memo</summary>

* DP from two sides
	- max profit from left till i
	- max profit from right till j
	- Find i == j where total profit is max

</details>

#### 125. Valid Palindrome
<details>
<summary>See Memo</summary>

* Two pointers
* Use isalnum()

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

</details>

#### 136. Single Number
<details>
<summary>See Memo</summary>

* Bit manipulation XOR
	* 0 ^ a = a
	* a ^ a = 0
	* a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b

</details>

</details>

#### Template
<details>
<summary>See Memo</summary>

</details>
